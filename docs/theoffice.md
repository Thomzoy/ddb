# The Office Awesome List

## A random quote 

<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-csv/1.0.21/jquery.csv.min.js"></script>
</head>


<audio title="truc" id="audio" controls="controls">
  <source id="audioSource" type="audio/mp3" src=""></source>
</audio>

## A random linguistic 

<div id="player"></div>

<iframe id="ytplayer" type="text/html" width="640" height="360"
  src=""
  frameborder="0"></iframe>



<script>

function pickQuote(){

    $.ajax({
      type: "GET",  
      url: "../_static/theoffice/quotes.csv",
      dataType: "text",       
      success: function(response)  
      {
        var quotes = $.csv.toArrays(response);
        var quote = quotes[Math.floor(Math.random()*quotes.length)];
        console.log(quote + ".mp3")
        var audio = document.getElementById('audio');
        var source = document.getElementById('audioSource');
        console.log(quote);
        source.src = escape("../_static/theoffice/" + quote + ".mp3");
        audio.load(); 

        //var quoteTitle = $("#quote-title").html(quote)
      }   
    });
};

function pickVideo(){

    $.ajax({
      type: "GET",  
      url: "../_static/theoffice/videos.csv",
      dataType: "text",       
      success: function(response)  
      {
        var videos = $.csv.toArrays(response);
        var video = videos[Math.floor(Math.random()*videos.length)];
        console.log(video)
        var player = document.getElementById('ytplayer');
        player.src = "https://www.youtube.com/embed/" + video;
        console.log(player.src)
      }   
    });
};


window.onload=pickQuote;
window.onload=pickVideo;

</script>