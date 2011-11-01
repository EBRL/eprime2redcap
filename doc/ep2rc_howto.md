Intro
=====

`ep2rc` is the system that takes exported data from E-prime, parses it, "runs the macro", and uploads the results to our In-Magnet Master Redcap database.

There are a couple of ways to use the system.  The easiest way is to use the [web application][ep2rc_web]. This site is password-protected, so if you need access tell Scott.

The other, considerably more difficult, way to use the application is to download the code and run it yourself.  If you're interested, ask Scott how to go about doing this.

Using the website
-----------------

When you first go to the [website][ep2rc_web], you'll need to authenticate yourself.  Assuming you've done this correctly, you'll be presented with the main page, which is the subject information page. You'll need to enter information into each of the pertinent fields.  

However, not all of the fields are required for every task.  For instance, only the NF grant uses the "Visit" field.  Also, some tasks do not have an associated list (NF's MI, for instance), so if you were uploading that task you wouldn't need to fill out that field. Don't forget to put in your name, it's useful for our logs.

When the fields are complete, click on the `submit` button. On the next page, if the data you're uploading is already in the database, you'll be warned.  If this happens, you may just want to start over and enter the information again. Do this by clicking on the link beneath the buttons.

Otherwise, click on the `Choose File` button and select the [properly named][naming] file that you exported from E-Data Aid. The filename will be displayed next to the `Choose File` button. Click `Submit` and *hopefully* everything will succeed!

If it doesn't succeed, the values that would be sent to Redcap are printed on the page so you can manually import them. When this happens, please send Scott an email and if possible attach the file that you tried to upload.

**Regardless of what the page says, always check Redcap to make sure the values were imported**

[ep2rc_web]: http://cutting.accre.vanderbilt.edu:8080
[naming]: https://my.vanderbilt.edu/ebrl/2011/10/e-prime-export-howto/