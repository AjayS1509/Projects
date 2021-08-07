<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Slidebar</title>
    <link rel="stylesheet" type = "text/css" href="css/bootstrap.min.css">
    <script type="text/javascript" src="js/bootstrap.js">
    </script>
    <script type="text/javascript" src="other/jquery-3.6.0.min.js">
    </script>
    <script type="text/javascript"src="other/popper.min.js">
    </script>


  </head>
  <body>
    <div id="carouselExampleIndicators" class="carousel slide" data-mdb-ride="carousel">
  <div class="carousel-indicators">
    <button
      type="button"
      data-mdb-target="#carouselExampleIndicators"
      data-mdb-slide-to="0"
      class="active"
      aria-current="true"
      aria-label="Slide 1"
    ></button>
    <button
      type="button"
      data-mdb-target="#carouselExampleIndicators"
      data-mdb-slide-to="1"
      aria-label="Slide 2"
    ></button>
    <button
      type="button"
      data-mdb-target="#carouselExampleIndicators"
      data-mdb-slide-to="2"
      aria-label="Slide 3"
    ></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img
        src="https://mdbootstrap.com/img/new/slides/041.jpg"
        class="d-block w-100"
        alt="..."
      />
    </div>
    <div class="carousel-item">
      <img
        src="https://mdbootstrap.com/img/new/slides/042.jpg"
        class="d-block w-100"
        alt="..."
      />
    </div>
    <div class="carousel-item">
      <img
        src="https://mdbootstrap.com/img/new/slides/043.jpg"
        class="d-block w-100"
        alt="..."
      />
    </div>
  </div>
  <button
    class="carousel-control-prev"
    type="button"
    data-mdb-target="#carouselExampleIndicators"
    data-mdb-slide="prev"
  >
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button
    class="carousel-control-next"
    type="button"
    data-mdb-target="#carouselExampleIndicators"
    data-mdb-slide="next"
  >
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
  </body>

</html>
