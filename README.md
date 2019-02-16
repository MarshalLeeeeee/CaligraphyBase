<h1> CaligraphyBase </h1>
<p> Scripts for setting up the dataset of caligraphy images <a href = "http://www.sfzd.cn/">↗</a>. </p>
<p> I consider common 3500 Chinese characters (shown in <b>simp.txt</b> and <b>comp.txt</b> (encoded in UTF-8)). </p>

<h3> Requirements </h3>
<ul type="circle">
  <li>requests</li>
  <li>re</li>
  <li>cv2</li>
  <li>numpy</li>
  <li>pypinyin</li>
  <li>bs4</li>
  <li>PIL</li>
</ul>

<h3> Run </h3>
<p>==================================================================</p>
<p><b> python cut.py </b></p>
<p> I pre-generate the screenprints consisting of multiple characters (saved in <a href = "https://github.com/MarshalLeeeeee/CaligraphyBase/tree/master/raw">here</a>). To collect the SONG font of every 3500 characters, run this script to cut it into seperate image for every distinct character.</p>

<p>==================================================================</p>
<p><b> python spider.py [AUTHOR_NAME] </b></p>
<p> The [AUTHOR_NAME] should be in Chinese due to the source information. </p>
<p> For example, run <b> python spider.py 王羲之 </b> to collect the caligraphy characters of 王羲之. </p>
