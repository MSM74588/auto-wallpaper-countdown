# Countdown Wallpaper Creator
- ```cd ~```
- ```git clone https://github.com/MSM74588/auto-wallpaper-countdown.git```

Add this as a startup using gnome autostart configurator (Startup application)
- command: ``` bash -c "/usr/bin/python3 /home/$(whoami)/image-gen-python/main.py" ```

### Install pip dependencies
```bash
pip install -r requirements.txt
```

- to create requirements.txt use 'freeze' pkg
    - ``` pipreqs . ```
    - ```pip install pipreqs ``` - if not installed

