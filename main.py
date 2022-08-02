import archinstall

def main():
    try:
        if not archinstall.check_mirror_reachable():
            print("Mirror is not reachable. Please check your internet connection.")
            return
    except:
        pass

    disk = archinstall.select_disk(archinstall.all_blockdevices(partitions=False))
    disk.keep_partitions = False

    with archinstall.Filesystem(disk, archinstall.GPT) as fs:
        fs.load_layout(archinstall.select_disk_layout())

    with archinstall.Installer("/mnt") as installer:
        installer.add_bootloader(archinstall.ask_for_bootloader())

if __name__ == "__main__":
    main()
