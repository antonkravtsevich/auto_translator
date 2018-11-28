# Wow, it's auto translator!

Why i should use it?

**Becouse it automatically translates all your english text!**

Wow, it's so cool!

**Here's what you need to do:**

1. **Install python 3**
2. **Install all dependencies by typing command `pip install -r requirements.txt`**
3. **Run auto translation by typing command `python auto_translate.py %filename%` any time you need!**

Wow, it's save so much free time!

## Some useful information
This program translate docx file with a table, that look like this:

<table align="center">
    <tr>
        <td align="center">Text with translation</td>
        <td align="center">Текст с переводом</td>
    <tr>
    </tr>
        <td align="center">Text without translation</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">Some more text without translation</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center"><p></p></td>
        <td align="center"></td>
    </tr>
</table>

So, english articles in left column, their translation - in right column. This programm will translate all articles withowt translation (i.e. if their left cell is empty) and store translated text in left cell.

Table will lock like this:

<table align="center">
    <tr>
        <td align="center">Text with translation</td>
        <td align="center">Текст с переводом</td>
    <tr>
    </tr>
        <td align="center">Text without translation</td>
        <td align="center">Текст без перевода</td>
    </tr>
    <tr>
        <td align="center">Some more text without translation</td>
        <td align="center">Еще один текст без перевода</td>
    </tr>
    <tr>
        <td align="center"><p></p></td>
        <td align="center"></td>
    </tr>
</table>

After translation os compleate, file will be saved with name 'auto_translated__' + old file name.

Enjoy!