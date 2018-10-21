---
layout: default
---

# Test Image Post form

<form id="imgForm" enctype="multipart/form-data">
  <div>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"/>
  </div>
  <div>
    <label for="album">Album:</label>
    <input type="text" id="album" name="album"/>
  </div>
  <div>
    <label for="file">Choose file to upload</label>
    <input type="file" id="image" name="image">
  </div>
</form>

<div>
   <button onClick="run()">Submit</button>
 </div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="/assets/js/test/img_post.min.js"><script>