def FullOTA_InstallEnd(info):
    info.script.AppendExtra('run_program("/sbin/mount", "-t", "auto", "/system_root");');
    info.script.AppendExtra('run_program("/sbin/sed", "-i", "/exfat/d", "/system_root/system/etc/selinux/plat_sepolicy.cil");');
    info.script.AppendExtra('run_program("/sbin/sed", "-i", "/sdfat/d", "/system_root/system/etc/selinux/plat_sepolicy.cil");');
    info.script.AppendExtra('run_program("/sbin/sed", "-i", "-e", "$akey 703 ASSIST", "/system_root/system/usr/keylayout/Generic.kl");');
    info.script.AppendExtra('run_program("/sbin/umount", "-t", "auto", "/system_root");');
