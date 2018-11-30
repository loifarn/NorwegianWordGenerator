function switch_theme() {
    var mode = Cookies.get('theme');
    if (mode == null) {
        Cookies.set('theme', 'light');
    }
    if (mode == 'dark') { 
        Cookies.set('theme', 'light');
     }
    if (mode == 'light') {
        Cookies.set('theme', 'dark');
    }
    apply_theme();
}

function apply_theme() {
    var mode = Cookies.get('theme');

    if (mode == 'dark') {
        document.body.style.backgroundColor = "black";
        document.getElementById("words").style.color = "white";
        document.getElementById("NO_FLAG").src = "static/flag_dark.gif";
    }
    if (mode == 'light') {
        document.body.style.backgroundColor = "white";
        document.getElementById("words").style.color = "black";
        document.getElementById("NO_FLAG").src = "static/flag_light.gif";
    }
}