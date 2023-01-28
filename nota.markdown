<p align="center">
    <img src="https://i.ibb.co/kX6zMZp/Nota-logo-3-2-round.png" alt="Logo" width=100 height=100>
  </a>
  <p align="center">
    <b>Manage your notes!</b>
    <br>
    <a href="https://discord.gg/yf3jehq4sn">Support</a>
  </p>
</p>

<br>

<h1 align="center">Getting started</h1>

<center>

Nota's default prefix is **`-`**. You can change it later if needed.

To get a menu with all commands and some extra information, Type `-help`.

If you have any **problems** or **questions**, join the support server by clicking `Support` above.

</center>

<br>

<h1 align="center">Features</h1>
<h6 align="center">- Saving texts and attachments</h6>
<h6 align="center">- Editing already saved files</h6>
<h6 align="center">- Settings</h6>
<h6 align="center">- Fun commands</h6>

<br>

<h1 align="center">Help</h1>
<center>

If an argument is surrounded by `<>`, it is [**required**](https://top.gg/bot/670754613820915714) to use that argument.

If an argument is surrounded by `[]`, it is [**not required**](https://top.gg/bot/670754613820915714)  to use that argument

</center>

# File Commands
> File Saving
- **Saving normal text |** `-save text` `<name>` `<text>`
- **Saving raw text |** `-save raw` `<name>` `<text>`
- **Saving attachments |** `-save file` `<name>` `<file type>` `[message]`

> File Editing
- **Adding text |** `-save edit add` `<name>` `<text>`
- **Adding lines |** `-save edit addline` `<name>` `<text>`
- **Overwriting files |** `-save edit set` `<name>` `<new text>`
- **Overwriting lines |** `-save edit setline` `<name>` `<line>` `<new text>`
- **Removing text |** `-save edit remove` `<name>` `<text>`
- **Removing lines |** `-save edit removeline` `<name>` `<line>` `<new text>`

> File Favourites (Quick-Access)
- **Showing your favourites |** `-favourites`
- **Adding favourites |** `-favourites add` `<name>`
- **Removing favourites |** `-favourites remove` `<name>`

> Other File Commands
- **Reading files |** `-read` `<name>`
- **Deleting files |** `-delete` `<name>`
- **Listing all files |** `-files`

# Other Commands
> Settings
- **Setting the prefix |** `-setprefix` `<new prefix>`

> Statistics
- **Showing your statistics |** `-stats`
- **Showing Nota's statistics |** `-botstats`

> Fun Commands
- **Solving math problems |** `-calc` `<problem>`
- **Making simple custom embeds |** `-embed` `<title>` `<content>`

# Premium Commands
> Color
- **Setting the embed color |** `-setcolor` `<color hex>`
- **Resetting the embed color |** `-resetcolor`

> Toggles
- **Toggling the info footer |** `-togglefooter`
- **Toggling the advertisements |** `-toggleads`
- **Toggling the favourites dock |** `-togglefavourites`

> Other
- **Showing the current premium status |** `-premium`

<style>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap');
* {
    outline: 0;
}
  body {
    padding: 0px;
    margin: 0px;
    font-family: 'Roboto', sans-serif;
    overflow-x: hidden;
    color: var(--font-color);
    height: 100%;
    animation: Gradient 10s ease-in-out infinite;
    background: -webkit-linear-gradient(270deg, rgba(14, 198, 189, 1) 0%, rgba(104, 198, 14, 1) 100%);
    background: linear-gradient(270deg, rgba(14, 198, 189, 1) 0%, rgba(104, 198, 14, 1) 100%);
    filter: progid: DXImageTransform.Microsoft.gradient(startColorstr=rgba(14, 198, 189, 1), endColorstr=rgba(104, 198, 14, 1), GradientType=1);
    background-size: 300% 300%;
    background-position: left top;
  }
  pre, code {
  background: rgb(1,1,1,0.5);
  color: #ffffff;
  }

@keyframes Gradient {
    0% {
        background-position: left top
    }
    35% {
        background-position: center center
    }
    50% {
        background-position: right bottom
    }
    75% {
        background-position: center center
    }
    100% {
        background-position: left top
    }
}

.entity-hint,
.horizontal-separator {
display:none;
}

[data-theme=dark]{
    --border-subtle-thin: none;
    --background-tertiary: rgba(0,0,0,.4);
    --background-secondary: rgba(0,0,0,.4);
    --text-erased: rgba(255,255,255,.6);
}
[data-theme=light]{
    --border-subtle-thin: none;
    --background-tertiary: rgba(0,0,0,.4);
    --background-secondary: rgba(0,0,0,.4);
    --text-erased: rgba(255,255,255,.6);
}
</style>