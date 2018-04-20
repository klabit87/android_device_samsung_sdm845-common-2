def FullOTA_InstallEnd(info):
    info.script.AppendExtra('run_program("/sbin/mount", "-t", "auto", "/system");');
    info.script.AppendExtra('run_program("/sbin/sed", "-i", "/exfat/d", "/system/system/etc/selinux/plat_sepolicy.cil");');
    info.script.AppendExtra('run_program("/sbin/sed", "-i", "/sdfat/d", "/system/system/etc/selinux/plat_sepolicy.cil");');
    info.script.AppendExtra('run_program("/sbin/sed", "-i", "-e", "$akey 703 ASSIST", "/system/usr/keylayout/Generic.kl");');
    info.script.AppendExtra('run_program("/sbin/umount", "-t", "auto", "/system");');
