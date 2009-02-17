# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.35
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _selinux
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


import shutil, os, stat

def restorecon(path, recursive=False):
    """ Restore SELinux context on a given path """
    mode = os.lstat(path)[stat.ST_MODE]
    status, context = matchpathcon(path, mode)
    if status == 0:
        lsetfilecon(path, context)
        if recursive:
            os.path.walk(path, lambda arg, dirname, fnames:
                             map(restorecon, [os.path.join(dirname, fname)
                                              for fname in fnames]), None)


is_selinux_enabled = _selinux.is_selinux_enabled
is_selinux_mls_enabled = _selinux.is_selinux_mls_enabled
getcon = _selinux.getcon
getcon_raw = _selinux.getcon_raw
setcon = _selinux.setcon
setcon_raw = _selinux.setcon_raw
getpidcon = _selinux.getpidcon
getpidcon_raw = _selinux.getpidcon_raw
getprevcon = _selinux.getprevcon
getprevcon_raw = _selinux.getprevcon_raw
getexeccon = _selinux.getexeccon
getexeccon_raw = _selinux.getexeccon_raw
setexeccon = _selinux.setexeccon
setexeccon_raw = _selinux.setexeccon_raw
getfscreatecon = _selinux.getfscreatecon
getfscreatecon_raw = _selinux.getfscreatecon_raw
setfscreatecon = _selinux.setfscreatecon
setfscreatecon_raw = _selinux.setfscreatecon_raw
getkeycreatecon = _selinux.getkeycreatecon
getkeycreatecon_raw = _selinux.getkeycreatecon_raw
setkeycreatecon = _selinux.setkeycreatecon
setkeycreatecon_raw = _selinux.setkeycreatecon_raw
getsockcreatecon = _selinux.getsockcreatecon
getsockcreatecon_raw = _selinux.getsockcreatecon_raw
setsockcreatecon = _selinux.setsockcreatecon
setsockcreatecon_raw = _selinux.setsockcreatecon_raw
getfilecon = _selinux.getfilecon
getfilecon_raw = _selinux.getfilecon_raw
lgetfilecon = _selinux.lgetfilecon
lgetfilecon_raw = _selinux.lgetfilecon_raw
fgetfilecon = _selinux.fgetfilecon
fgetfilecon_raw = _selinux.fgetfilecon_raw
setfilecon = _selinux.setfilecon
setfilecon_raw = _selinux.setfilecon_raw
lsetfilecon = _selinux.lsetfilecon
lsetfilecon_raw = _selinux.lsetfilecon_raw
fsetfilecon = _selinux.fsetfilecon
fsetfilecon_raw = _selinux.fsetfilecon_raw
getpeercon = _selinux.getpeercon
getpeercon_raw = _selinux.getpeercon_raw
class av_decision(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, av_decision, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, av_decision, name)
    __repr__ = _swig_repr
    __swig_setmethods__["allowed"] = _selinux.av_decision_allowed_set
    __swig_getmethods__["allowed"] = _selinux.av_decision_allowed_get
    if _newclass:allowed = _swig_property(_selinux.av_decision_allowed_get, _selinux.av_decision_allowed_set)
    __swig_setmethods__["decided"] = _selinux.av_decision_decided_set
    __swig_getmethods__["decided"] = _selinux.av_decision_decided_get
    if _newclass:decided = _swig_property(_selinux.av_decision_decided_get, _selinux.av_decision_decided_set)
    __swig_setmethods__["auditallow"] = _selinux.av_decision_auditallow_set
    __swig_getmethods__["auditallow"] = _selinux.av_decision_auditallow_get
    if _newclass:auditallow = _swig_property(_selinux.av_decision_auditallow_get, _selinux.av_decision_auditallow_set)
    __swig_setmethods__["auditdeny"] = _selinux.av_decision_auditdeny_set
    __swig_getmethods__["auditdeny"] = _selinux.av_decision_auditdeny_get
    if _newclass:auditdeny = _swig_property(_selinux.av_decision_auditdeny_get, _selinux.av_decision_auditdeny_set)
    __swig_setmethods__["seqno"] = _selinux.av_decision_seqno_set
    __swig_getmethods__["seqno"] = _selinux.av_decision_seqno_get
    if _newclass:seqno = _swig_property(_selinux.av_decision_seqno_get, _selinux.av_decision_seqno_set)
    def __init__(self, *args): 
        this = _selinux.new_av_decision(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _selinux.delete_av_decision
    __del__ = lambda self : None;
av_decision_swigregister = _selinux.av_decision_swigregister
av_decision_swigregister(av_decision)

class selinux_opt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, selinux_opt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, selinux_opt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _selinux.selinux_opt_type_set
    __swig_getmethods__["type"] = _selinux.selinux_opt_type_get
    if _newclass:type = _swig_property(_selinux.selinux_opt_type_get, _selinux.selinux_opt_type_set)
    __swig_setmethods__["value"] = _selinux.selinux_opt_value_set
    __swig_getmethods__["value"] = _selinux.selinux_opt_value_get
    if _newclass:value = _swig_property(_selinux.selinux_opt_value_get, _selinux.selinux_opt_value_set)
    def __init__(self, *args): 
        this = _selinux.new_selinux_opt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _selinux.delete_selinux_opt
    __del__ = lambda self : None;
selinux_opt_swigregister = _selinux.selinux_opt_swigregister
selinux_opt_swigregister(selinux_opt)

class selinux_callback(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, selinux_callback, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, selinux_callback, name)
    __repr__ = _swig_repr
    __swig_setmethods__["func_log"] = _selinux.selinux_callback_func_log_set
    __swig_getmethods__["func_log"] = _selinux.selinux_callback_func_log_get
    if _newclass:func_log = _swig_property(_selinux.selinux_callback_func_log_get, _selinux.selinux_callback_func_log_set)
    __swig_setmethods__["func_audit"] = _selinux.selinux_callback_func_audit_set
    __swig_getmethods__["func_audit"] = _selinux.selinux_callback_func_audit_get
    if _newclass:func_audit = _swig_property(_selinux.selinux_callback_func_audit_get, _selinux.selinux_callback_func_audit_set)
    __swig_setmethods__["func_validate"] = _selinux.selinux_callback_func_validate_set
    __swig_getmethods__["func_validate"] = _selinux.selinux_callback_func_validate_get
    if _newclass:func_validate = _swig_property(_selinux.selinux_callback_func_validate_get, _selinux.selinux_callback_func_validate_set)
    def __init__(self, *args): 
        this = _selinux.new_selinux_callback(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _selinux.delete_selinux_callback
    __del__ = lambda self : None;
selinux_callback_swigregister = _selinux.selinux_callback_swigregister
selinux_callback_swigregister(selinux_callback)

SELINUX_CB_LOG = _selinux.SELINUX_CB_LOG
SELINUX_CB_AUDIT = _selinux.SELINUX_CB_AUDIT
SELINUX_CB_VALIDATE = _selinux.SELINUX_CB_VALIDATE
selinux_get_callback = _selinux.selinux_get_callback
selinux_set_callback = _selinux.selinux_set_callback
SELINUX_ERROR = _selinux.SELINUX_ERROR
SELINUX_WARNING = _selinux.SELINUX_WARNING
SELINUX_INFO = _selinux.SELINUX_INFO
SELINUX_AVC = _selinux.SELINUX_AVC
security_compute_av = _selinux.security_compute_av
security_compute_av_raw = _selinux.security_compute_av_raw
security_compute_create = _selinux.security_compute_create
security_compute_create_raw = _selinux.security_compute_create_raw
security_compute_relabel = _selinux.security_compute_relabel
security_compute_relabel_raw = _selinux.security_compute_relabel_raw
security_compute_member = _selinux.security_compute_member
security_compute_member_raw = _selinux.security_compute_member_raw
security_compute_user = _selinux.security_compute_user
security_compute_user_raw = _selinux.security_compute_user_raw
security_load_policy = _selinux.security_load_policy
security_get_initial_context = _selinux.security_get_initial_context
security_get_initial_context_raw = _selinux.security_get_initial_context_raw
selinux_mkload_policy = _selinux.selinux_mkload_policy
selinux_init_load_policy = _selinux.selinux_init_load_policy
class SELboolean(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SELboolean, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SELboolean, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _selinux.SELboolean_name_set
    __swig_getmethods__["name"] = _selinux.SELboolean_name_get
    if _newclass:name = _swig_property(_selinux.SELboolean_name_get, _selinux.SELboolean_name_set)
    __swig_setmethods__["value"] = _selinux.SELboolean_value_set
    __swig_getmethods__["value"] = _selinux.SELboolean_value_get
    if _newclass:value = _swig_property(_selinux.SELboolean_value_get, _selinux.SELboolean_value_set)
    def __init__(self, *args): 
        this = _selinux.new_SELboolean(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _selinux.delete_SELboolean
    __del__ = lambda self : None;
SELboolean_swigregister = _selinux.SELboolean_swigregister
SELboolean_swigregister(SELboolean)

security_set_boolean_list = _selinux.security_set_boolean_list
security_load_booleans = _selinux.security_load_booleans
security_check_context = _selinux.security_check_context
security_check_context_raw = _selinux.security_check_context_raw
security_canonicalize_context = _selinux.security_canonicalize_context
security_canonicalize_context_raw = _selinux.security_canonicalize_context_raw
security_getenforce = _selinux.security_getenforce
security_setenforce = _selinux.security_setenforce
security_disable = _selinux.security_disable
security_policyvers = _selinux.security_policyvers
security_get_boolean_names = _selinux.security_get_boolean_names
security_get_boolean_pending = _selinux.security_get_boolean_pending
security_get_boolean_active = _selinux.security_get_boolean_active
security_set_boolean = _selinux.security_set_boolean
security_commit_booleans = _selinux.security_commit_booleans
class security_class_mapping(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, security_class_mapping, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, security_class_mapping, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _selinux.security_class_mapping_name_set
    __swig_getmethods__["name"] = _selinux.security_class_mapping_name_get
    if _newclass:name = _swig_property(_selinux.security_class_mapping_name_get, _selinux.security_class_mapping_name_set)
    __swig_setmethods__["perms"] = _selinux.security_class_mapping_perms_set
    __swig_getmethods__["perms"] = _selinux.security_class_mapping_perms_get
    if _newclass:perms = _swig_property(_selinux.security_class_mapping_perms_get, _selinux.security_class_mapping_perms_set)
    def __init__(self, *args): 
        this = _selinux.new_security_class_mapping(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _selinux.delete_security_class_mapping
    __del__ = lambda self : None;
security_class_mapping_swigregister = _selinux.security_class_mapping_swigregister
security_class_mapping_swigregister(security_class_mapping)

selinux_set_mapping = _selinux.selinux_set_mapping
string_to_security_class = _selinux.string_to_security_class
security_class_to_string = _selinux.security_class_to_string
security_av_perm_to_string = _selinux.security_av_perm_to_string
string_to_av_perm = _selinux.string_to_av_perm
security_av_string = _selinux.security_av_string
print_access_vector = _selinux.print_access_vector
MATCHPATHCON_BASEONLY = _selinux.MATCHPATHCON_BASEONLY
MATCHPATHCON_NOTRANS = _selinux.MATCHPATHCON_NOTRANS
MATCHPATHCON_VALIDATE = _selinux.MATCHPATHCON_VALIDATE
set_matchpathcon_flags = _selinux.set_matchpathcon_flags
matchpathcon_init = _selinux.matchpathcon_init
matchpathcon_init_prefix = _selinux.matchpathcon_init_prefix
matchpathcon_fini = _selinux.matchpathcon_fini
matchpathcon = _selinux.matchpathcon
matchpathcon_index = _selinux.matchpathcon_index
matchpathcon_filespec_add = _selinux.matchpathcon_filespec_add
matchpathcon_filespec_destroy = _selinux.matchpathcon_filespec_destroy
matchpathcon_filespec_eval = _selinux.matchpathcon_filespec_eval
matchpathcon_checkmatches = _selinux.matchpathcon_checkmatches
matchmediacon = _selinux.matchmediacon
selinux_getenforcemode = _selinux.selinux_getenforcemode
selinux_getpolicytype = _selinux.selinux_getpolicytype
selinux_policy_root = _selinux.selinux_policy_root
selinux_binary_policy_path = _selinux.selinux_binary_policy_path
selinux_failsafe_context_path = _selinux.selinux_failsafe_context_path
selinux_removable_context_path = _selinux.selinux_removable_context_path
selinux_default_context_path = _selinux.selinux_default_context_path
selinux_user_contexts_path = _selinux.selinux_user_contexts_path
selinux_file_context_path = _selinux.selinux_file_context_path
selinux_file_context_homedir_path = _selinux.selinux_file_context_homedir_path
selinux_file_context_local_path = _selinux.selinux_file_context_local_path
selinux_homedir_context_path = _selinux.selinux_homedir_context_path
selinux_media_context_path = _selinux.selinux_media_context_path
selinux_x_context_path = _selinux.selinux_x_context_path
selinux_contexts_path = _selinux.selinux_contexts_path
selinux_securetty_types_path = _selinux.selinux_securetty_types_path
selinux_booleans_path = _selinux.selinux_booleans_path
selinux_customizable_types_path = _selinux.selinux_customizable_types_path
selinux_users_path = _selinux.selinux_users_path
selinux_usersconf_path = _selinux.selinux_usersconf_path
selinux_translations_path = _selinux.selinux_translations_path
selinux_colors_path = _selinux.selinux_colors_path
selinux_netfilter_context_path = _selinux.selinux_netfilter_context_path
selinux_path = _selinux.selinux_path
selinux_check_passwd_access = _selinux.selinux_check_passwd_access
checkPasswdAccess = _selinux.checkPasswdAccess
selinux_check_securetty_context = _selinux.selinux_check_securetty_context
set_selinuxmnt = _selinux.set_selinuxmnt
rpm_execcon = _selinux.rpm_execcon
is_context_customizable = _selinux.is_context_customizable
selinux_trans_to_raw_context = _selinux.selinux_trans_to_raw_context
selinux_raw_to_trans_context = _selinux.selinux_raw_to_trans_context
selinux_raw_context_to_color = _selinux.selinux_raw_context_to_color
getseuserbyname = _selinux.getseuserbyname
selinux_file_context_cmp = _selinux.selinux_file_context_cmp
selinux_file_context_verify = _selinux.selinux_file_context_verify
selinux_lsetfilecon_default = _selinux.selinux_lsetfilecon_default
class security_id(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, security_id, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, security_id, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ctx"] = _selinux.security_id_ctx_set
    __swig_getmethods__["ctx"] = _selinux.security_id_ctx_get
    if _newclass:ctx = _swig_property(_selinux.security_id_ctx_get, _selinux.security_id_ctx_set)
    __swig_setmethods__["refcnt"] = _selinux.security_id_refcnt_set
    __swig_getmethods__["refcnt"] = _selinux.security_id_refcnt_get
    if _newclass:refcnt = _swig_property(_selinux.security_id_refcnt_get, _selinux.security_id_refcnt_set)
    def __init__(self, *args): 
        this = _selinux.new_security_id(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _selinux.delete_security_id
    __del__ = lambda self : None;
security_id_swigregister = _selinux.security_id_swigregister
security_id_swigregister(security_id)

avc_sid_to_context = _selinux.avc_sid_to_context
avc_sid_to_context_raw = _selinux.avc_sid_to_context_raw
avc_context_to_sid = _selinux.avc_context_to_sid
avc_context_to_sid_raw = _selinux.avc_context_to_sid_raw
sidget = _selinux.sidget
sidput = _selinux.sidput
avc_get_initial_sid = _selinux.avc_get_initial_sid
class avc_entry_ref(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, avc_entry_ref, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, avc_entry_ref, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ae"] = _selinux.avc_entry_ref_ae_set
    __swig_getmethods__["ae"] = _selinux.avc_entry_ref_ae_get
    if _newclass:ae = _swig_property(_selinux.avc_entry_ref_ae_get, _selinux.avc_entry_ref_ae_set)
    def __init__(self, *args): 
        this = _selinux.new_avc_entry_ref(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _selinux.delete_avc_entry_ref
    __del__ = lambda self : None;
avc_entry_ref_swigregister = _selinux.avc_entry_ref_swigregister
avc_entry_ref_swigregister(avc_entry_ref)

class avc_memory_callback(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, avc_memory_callback, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, avc_memory_callback, name)
    __repr__ = _swig_repr
    __swig_setmethods__["func_malloc"] = _selinux.avc_memory_callback_func_malloc_set
    __swig_getmethods__["func_malloc"] = _selinux.avc_memory_callback_func_malloc_get
    if _newclass:func_malloc = _swig_property(_selinux.avc_memory_callback_func_malloc_get, _selinux.avc_memory_callback_func_malloc_set)
    __swig_setmethods__["func_free"] = _selinux.avc_memory_callback_func_free_set
    __swig_getmethods__["func_free"] = _selinux.avc_memory_callback_func_free_get
    if _newclass:func_free = _swig_property(_selinux.avc_memory_callback_func_free_get, _selinux.avc_memory_callback_func_free_set)
    def __init__(self, *args): 
        this = _selinux.new_avc_memory_callback(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _selinux.delete_avc_memory_callback
    __del__ = lambda self : None;
avc_memory_callback_swigregister = _selinux.avc_memory_callback_swigregister
avc_memory_callback_swigregister(avc_memory_callback)

class avc_log_callback(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, avc_log_callback, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, avc_log_callback, name)
    __repr__ = _swig_repr
    __swig_setmethods__["func_log"] = _selinux.avc_log_callback_func_log_set
    __swig_getmethods__["func_log"] = _selinux.avc_log_callback_func_log_get
    if _newclass:func_log = _swig_property(_selinux.avc_log_callback_func_log_get, _selinux.avc_log_callback_func_log_set)
    __swig_setmethods__["func_audit"] = _selinux.avc_log_callback_func_audit_set
    __swig_getmethods__["func_audit"] = _selinux.avc_log_callback_func_audit_get
    if _newclass:func_audit = _swig_property(_selinux.avc_log_callback_func_audit_get, _selinux.avc_log_callback_func_audit_set)
    def __init__(self, *args): 
        this = _selinux.new_avc_log_callback(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _selinux.delete_avc_log_callback
    __del__ = lambda self : None;
avc_log_callback_swigregister = _selinux.avc_log_callback_swigregister
avc_log_callback_swigregister(avc_log_callback)

class avc_thread_callback(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, avc_thread_callback, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, avc_thread_callback, name)
    __repr__ = _swig_repr
    __swig_setmethods__["func_create_thread"] = _selinux.avc_thread_callback_func_create_thread_set
    __swig_getmethods__["func_create_thread"] = _selinux.avc_thread_callback_func_create_thread_get
    if _newclass:func_create_thread = _swig_property(_selinux.avc_thread_callback_func_create_thread_get, _selinux.avc_thread_callback_func_create_thread_set)
    __swig_setmethods__["func_stop_thread"] = _selinux.avc_thread_callback_func_stop_thread_set
    __swig_getmethods__["func_stop_thread"] = _selinux.avc_thread_callback_func_stop_thread_get
    if _newclass:func_stop_thread = _swig_property(_selinux.avc_thread_callback_func_stop_thread_get, _selinux.avc_thread_callback_func_stop_thread_set)
    def __init__(self, *args): 
        this = _selinux.new_avc_thread_callback(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _selinux.delete_avc_thread_callback
    __del__ = lambda self : None;
avc_thread_callback_swigregister = _selinux.avc_thread_callback_swigregister
avc_thread_callback_swigregister(avc_thread_callback)

class avc_lock_callback(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, avc_lock_callback, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, avc_lock_callback, name)
    __repr__ = _swig_repr
    __swig_setmethods__["func_alloc_lock"] = _selinux.avc_lock_callback_func_alloc_lock_set
    __swig_getmethods__["func_alloc_lock"] = _selinux.avc_lock_callback_func_alloc_lock_get
    if _newclass:func_alloc_lock = _swig_property(_selinux.avc_lock_callback_func_alloc_lock_get, _selinux.avc_lock_callback_func_alloc_lock_set)
    __swig_setmethods__["func_get_lock"] = _selinux.avc_lock_callback_func_get_lock_set
    __swig_getmethods__["func_get_lock"] = _selinux.avc_lock_callback_func_get_lock_get
    if _newclass:func_get_lock = _swig_property(_selinux.avc_lock_callback_func_get_lock_get, _selinux.avc_lock_callback_func_get_lock_set)
    __swig_setmethods__["func_release_lock"] = _selinux.avc_lock_callback_func_release_lock_set
    __swig_getmethods__["func_release_lock"] = _selinux.avc_lock_callback_func_release_lock_get
    if _newclass:func_release_lock = _swig_property(_selinux.avc_lock_callback_func_release_lock_get, _selinux.avc_lock_callback_func_release_lock_set)
    __swig_setmethods__["func_free_lock"] = _selinux.avc_lock_callback_func_free_lock_set
    __swig_getmethods__["func_free_lock"] = _selinux.avc_lock_callback_func_free_lock_get
    if _newclass:func_free_lock = _swig_property(_selinux.avc_lock_callback_func_free_lock_get, _selinux.avc_lock_callback_func_free_lock_set)
    def __init__(self, *args): 
        this = _selinux.new_avc_lock_callback(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _selinux.delete_avc_lock_callback
    __del__ = lambda self : None;
avc_lock_callback_swigregister = _selinux.avc_lock_callback_swigregister
avc_lock_callback_swigregister(avc_lock_callback)

AVC_OPT_UNUSED = _selinux.AVC_OPT_UNUSED
AVC_OPT_SETENFORCE = _selinux.AVC_OPT_SETENFORCE
avc_init = _selinux.avc_init
avc_open = _selinux.avc_open
avc_cleanup = _selinux.avc_cleanup
avc_reset = _selinux.avc_reset
avc_destroy = _selinux.avc_destroy
avc_has_perm_noaudit = _selinux.avc_has_perm_noaudit
avc_has_perm = _selinux.avc_has_perm
avc_audit = _selinux.avc_audit
avc_compute_create = _selinux.avc_compute_create
avc_compute_member = _selinux.avc_compute_member
AVC_CALLBACK_GRANT = _selinux.AVC_CALLBACK_GRANT
AVC_CALLBACK_TRY_REVOKE = _selinux.AVC_CALLBACK_TRY_REVOKE
AVC_CALLBACK_REVOKE = _selinux.AVC_CALLBACK_REVOKE
AVC_CALLBACK_RESET = _selinux.AVC_CALLBACK_RESET
AVC_CALLBACK_AUDITALLOW_ENABLE = _selinux.AVC_CALLBACK_AUDITALLOW_ENABLE
AVC_CALLBACK_AUDITALLOW_DISABLE = _selinux.AVC_CALLBACK_AUDITALLOW_DISABLE
AVC_CALLBACK_AUDITDENY_ENABLE = _selinux.AVC_CALLBACK_AUDITDENY_ENABLE
AVC_CALLBACK_AUDITDENY_DISABLE = _selinux.AVC_CALLBACK_AUDITDENY_DISABLE
AVC_CACHE_STATS = _selinux.AVC_CACHE_STATS
class avc_cache_stats(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, avc_cache_stats, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, avc_cache_stats, name)
    __repr__ = _swig_repr
    __swig_setmethods__["entry_lookups"] = _selinux.avc_cache_stats_entry_lookups_set
    __swig_getmethods__["entry_lookups"] = _selinux.avc_cache_stats_entry_lookups_get
    if _newclass:entry_lookups = _swig_property(_selinux.avc_cache_stats_entry_lookups_get, _selinux.avc_cache_stats_entry_lookups_set)
    __swig_setmethods__["entry_hits"] = _selinux.avc_cache_stats_entry_hits_set
    __swig_getmethods__["entry_hits"] = _selinux.avc_cache_stats_entry_hits_get
    if _newclass:entry_hits = _swig_property(_selinux.avc_cache_stats_entry_hits_get, _selinux.avc_cache_stats_entry_hits_set)
    __swig_setmethods__["entry_misses"] = _selinux.avc_cache_stats_entry_misses_set
    __swig_getmethods__["entry_misses"] = _selinux.avc_cache_stats_entry_misses_get
    if _newclass:entry_misses = _swig_property(_selinux.avc_cache_stats_entry_misses_get, _selinux.avc_cache_stats_entry_misses_set)
    __swig_setmethods__["entry_discards"] = _selinux.avc_cache_stats_entry_discards_set
    __swig_getmethods__["entry_discards"] = _selinux.avc_cache_stats_entry_discards_get
    if _newclass:entry_discards = _swig_property(_selinux.avc_cache_stats_entry_discards_get, _selinux.avc_cache_stats_entry_discards_set)
    __swig_setmethods__["cav_lookups"] = _selinux.avc_cache_stats_cav_lookups_set
    __swig_getmethods__["cav_lookups"] = _selinux.avc_cache_stats_cav_lookups_get
    if _newclass:cav_lookups = _swig_property(_selinux.avc_cache_stats_cav_lookups_get, _selinux.avc_cache_stats_cav_lookups_set)
    __swig_setmethods__["cav_hits"] = _selinux.avc_cache_stats_cav_hits_set
    __swig_getmethods__["cav_hits"] = _selinux.avc_cache_stats_cav_hits_get
    if _newclass:cav_hits = _swig_property(_selinux.avc_cache_stats_cav_hits_get, _selinux.avc_cache_stats_cav_hits_set)
    __swig_setmethods__["cav_probes"] = _selinux.avc_cache_stats_cav_probes_set
    __swig_getmethods__["cav_probes"] = _selinux.avc_cache_stats_cav_probes_get
    if _newclass:cav_probes = _swig_property(_selinux.avc_cache_stats_cav_probes_get, _selinux.avc_cache_stats_cav_probes_set)
    __swig_setmethods__["cav_misses"] = _selinux.avc_cache_stats_cav_misses_set
    __swig_getmethods__["cav_misses"] = _selinux.avc_cache_stats_cav_misses_get
    if _newclass:cav_misses = _swig_property(_selinux.avc_cache_stats_cav_misses_get, _selinux.avc_cache_stats_cav_misses_set)
    def __init__(self, *args): 
        this = _selinux.new_avc_cache_stats(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _selinux.delete_avc_cache_stats
    __del__ = lambda self : None;
avc_cache_stats_swigregister = _selinux.avc_cache_stats_swigregister
avc_cache_stats_swigregister(avc_cache_stats)

avc_av_stats = _selinux.avc_av_stats
avc_sid_stats = _selinux.avc_sid_stats
selinux_default_type_path = _selinux.selinux_default_type_path
get_default_type = _selinux.get_default_type
SELINUX_DEFAULTUSER = _selinux.SELINUX_DEFAULTUSER
get_ordered_context_list = _selinux.get_ordered_context_list
get_ordered_context_list_with_level = _selinux.get_ordered_context_list_with_level
get_default_context = _selinux.get_default_context
get_default_context_with_level = _selinux.get_default_context_with_level
get_default_context_with_role = _selinux.get_default_context_with_role
get_default_context_with_rolelevel = _selinux.get_default_context_with_rolelevel
query_user_context = _selinux.query_user_context
manual_user_enter_context = _selinux.manual_user_enter_context

