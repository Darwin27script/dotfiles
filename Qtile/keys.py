keys = [
    # Switch focus between windows
    Key([mod], "left", lazy.layout.left()),
    Key([mod], "right", lazy.layout.right()),
    Key([mod], "down", lazy.layout.down()),
    Key([mod], "up", lazy.layout.up()),

    # Move windows
    Key([mod, "shift"], "left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up()),

    # Launch Terminal
    Key([mod], "Return", lazy.spawn(terminal)),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),

    # Kill focus windows
    Key([mod], "w", lazy.window.kill()),
    
    # Toggle fullscreen on the focused window
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    # Toggle floating on the focused window
    Key([mod], "t", lazy.window.toggle_floating()),

    # reload the config
    Key([mod, "control"], "r", lazy.reload_config()),
    
    # Shutdown qtile
    Key([mod, "control"], "q", lazy.shutdown()),

    # ----ROFI----
    # Menu
    Key([mod], "r", lazy.spawn("rofi -show drun")),
    # Menu nav
    Key([mod], "m", lazy.spawn("rofi -show")),

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),    
]