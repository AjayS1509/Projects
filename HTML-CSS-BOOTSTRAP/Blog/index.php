<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <title></title>
    <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" type = "text/css" href="css/bootstrap.min.css">
  <script type="text/javascript" src="js/bootstrap.js">
  </script>
  <script type="text/javascript" src="other/jquery-3.6.0.min.js">
  </script>
  <script type="text/javascript"src="other/popper.min.js">
  </script>

  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Ajay's Blog</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="index.php">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Services</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="about.php">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Contact</a>
        </li>


      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>

<div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="images/a8.jpg"  class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>First slide label</h5>
        <p>Some representative placeholder content for the first slide.</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="images/a9.jpg" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Second slide label</h5>
        <p>Some representative placeholder content for the second slide.</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="images/a10.jpg" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Third slide label</h5>
        <p>Some representative placeholder content for the third slide.</p>
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
<section class="my-5">
  <div class="py-5">
    <h2 class = "text-center"> About Us</h2>
  </div>
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-6 col-md-6 col-12">
        <img src = "images/a1.jpg" class = "img-fluid">
      </div>
      <div class="col-lg-6 col-md-6 col-12">
        <h2 class = "display-4"> I am Ajay</h2>
          <p class = "py-5">A parachute uses drag to slow something moving in air.
            It is often an umbrella shaped device on which people or
             things can float slowly and safely down to the ground from
              a great height, such as an aircraft.</p>
          <a href = "about.php" class = "btn btn-success">Click Here</a>
      </div>
    </div>
  </div>

</section>

<section class="my-5">
  <div class="py-5">
    <h2 class = "text-center"> Our Services</h2>
  </div>
  <div class="container-fluid">
    <div class="row">
      <div class = "col-lg-4 col-md-4 col-12">
        <div class="card">
          <img class="card-img-top" src="images/a2.jpg" alt="Card image">
  <div class="card-body">
    <h4 class="card-title">Beautiful Nature </h4>
    <p class="card-text">Some example text.</p>
    <a href="#" class="btn btn-primary">See Profile</a>
  </div>
</div>
    </div>

    <div class = "col-lg-4 col-md-4 col-12">
      <div class="card">
        <img class="card-img-top" src="images/a3.jpg" alt="Card image">
<div class="card-body">
  <h4 class="card-title">Beautiful Nature </h4>
  <p class="card-text">Some example text.</p>
  <a href="#" class="btn btn-primary">See Profile</a>
</div>
</div>
  </div>

  <div class = "col-lg-4 col-md-4 col-12">
    <div class="card">
      <img class="card-img-top" src="images/a5.jpg" alt="Card image">
<div class="card-body">
<h4 class="card-title">Beautiful Nature </h4>
<p class="card-text">Some example text.</p>
<a href="#" class="btn btn-primary">See Profile</a>
</div>
</div>
</div>

  </div>
</div>
</section>

<section class = "my-5">
  <div class = "py-5">
    <h2 class = "text-center"> Our Gallary</h2>
  </div>
  <div class = "container-fluid">
    <div class="row">
      <div class = "col-lg-4 col-md-4 col-12">
        <img src = "images/a7.jpg" class = "image-fluid pb-3">
      </div>
      <div class = "col-lg-4 col-md-4 col-12">
        <img src = "images/a7.jpg" class = "image-fluid pb-3">
      </div>
      <div class = "col-lg-4 col-md-4 col-12">
        <img src = "images/a7.jpg" class = "image-fluid pb-3">
      </div>
      <div class = "col-lg-4 col-md-4 col-12">
        <img src = "images/a7.jpg" class = "image-fluid pb-3">
      </div>
      <div class = "col-lg-4 col-md-4 col-12">
        <img src = "images/a7.jpg" class = "image-fluid pb-3">
      </div>
      <div class = "col-lg-4 col-md-4 col-12">
        <img src = "images/a7.jpg" class = "image-fluid pb-3">
      </div>

    </div>
  </div>
</section>

<section class = "my-5">
  <div class = "py-5">
    <h2 class="text-center">Our Gallary</h2>
  </div>
  <div class ="w-50 m-auto">
    <form action ="userinfo.php" method ="post">
      <div class="form-group">
        <label>Username</label>
        <input type = "text" name = "user" autocomplete="off" class = "form-control">
      </div>
      <div class="form-group">
        <label>Email id</label>
        <input type = "text" name = "email" autocomplete="off" class = "form-control">
      </div>
      <div class="form-group">
        <label>Mobile No</label>
        <input type = "text" name = "mobile" autocomplete="off" class = "form-control">
      </div>
      <div class="form-group">
        <label>Comment</label>
        <textarea class = "form-control">
          </textarea
      </div>
       <button type="submit" class="btn btn-success">Submit</button>
    </form>
  </div>
</section>
<footer>
  <p class="p-3 bg-dark text-white">@Aj's Blog</p>
</footer>



    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  </body>

</html>
