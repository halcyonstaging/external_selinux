#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <ctype.h>
#include <stdio.h>
#include <stdio_ext.h>
#include <dlfcn.h>
#include <sys/vfs.h>
#include <stdint.h>
#include <limits.h>

#include "dso.h"
#include "policy.h"
#include "selinux_internal.h"
#include "setrans_internal.h"

char *selinux_mnt = NULL;
int selinux_page_size = 0;
int obj_class_compat = 1;

static void init_selinuxmnt(void)
{
	char *buf=NULL, *p;
	FILE *fp;
	struct statfs sfbuf;
	int rc;
	size_t len;
	ssize_t num;

	if (selinux_mnt)
		return;

	/* We check to see if the preferred mount point for selinux file
	 * system has a selinuxfs. */
	do {
		rc = statfs(SELINUXMNT, &sfbuf);
	} while (rc < 0 && errno == EINTR);
	if (rc == 0) {
		if ((uint32_t)sfbuf.f_type == (uint32_t)SELINUX_MAGIC) {
			selinux_mnt = strdup(SELINUXMNT);
			return;
		}
	} 

	/* At this point, the usual spot doesn't have an selinuxfs so
	 * we look around for it */
	fp = fopen("/proc/mounts", "r");
	if (!fp)
		return;

	__fsetlocking(fp, FSETLOCKING_BYCALLER);
	while ((num = getline(&buf, &len, fp)) != -1) {
		char *tmp;
		p = strchr(buf, ' ');
		if (!p)
			goto out;
		p++;
		tmp = strchr(p, ' ');
		if (!tmp)
			goto out;
		if (!strncmp(tmp + 1, "selinuxfs ", 10)) {
			*tmp = '\0';
			break;
		}
	}

	/* If we found something, dup it */
	if (num > 0)
		selinux_mnt = strdup(p);

      out:
	free(buf);
	fclose(fp);
	return;
}

static void fini_selinuxmnt(void)
{
	free(selinux_mnt);
	selinux_mnt = NULL;
}

void set_selinuxmnt(char *mnt)
{
	selinux_mnt = strdup(mnt);
}

hidden_def(set_selinuxmnt)

static void init_obj_class_compat(void)
{
	char path[PATH_MAX];
	struct stat s;

	if (!selinux_mnt)
		return;

	snprintf(path,PATH_MAX,"%s/class",selinux_mnt);
	if (stat(path,&s) < 0)
		return;

	if (S_ISDIR(s.st_mode))
		obj_class_compat = 0;
}

static void fini_obj_class_compat(void)
{
	obj_class_compat = 1;
}

static void init_lib(void) __attribute__ ((constructor));
static void init_lib(void)
{
	selinux_page_size = sysconf(_SC_PAGE_SIZE);
	init_selinuxmnt();
	init_obj_class_compat();
	init_context_translations();
}

static void fini_lib(void) __attribute__ ((destructor));
static void fini_lib(void)
{
	fini_selinuxmnt();
	fini_obj_class_compat();
	fini_context_translations();
}