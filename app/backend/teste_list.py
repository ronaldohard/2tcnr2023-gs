import json
import mysql.connector
from flask import Flask, render_template_string
from markupsafe import Markup

app = Flask(__name__)

db_config = {
    'host': '',
    'user': '',
    'password': '',
    'database': ''
}


def fetch_alunos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM tb_alunos"
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


@app.route('/alunos', methods=['GET'])
def alunos():

    # Finalmente, renderizamos o template para cada post.

    card_blog_template = """
            <div class="col-lg-4 col-md-4 col-sm-6">
                <div class="fh5co-blog animate-box">
                    <a href="#"><img class="img-responsive" src="{{ url_base }}/images/cover_bg_1.jpg" alt=""></a>
                    <div class="blog-text">
                        <div class="prod-title">
                            <h3><a href="#aiaiaiai">{{ aluno.aluno_email }}</a></h3>
                            <span class="posted_by">Sep. 15th</span>
                            <span class="comment"><a href="">21<i class="icon-bubble2"></i></a></span>
                            <p>Descriçao da solicitação de alimento # {{ aluno.aluno_endereco }}</p>
                            <p><a href="#">Saiba Mais...</a></p>
                        </div>
                    </div> 
                </div>
            </div>
    """

    card = ""

    print(fetch_alunos())

    for aluno in fetch_alunos():
        card += render_template_string(card_blog_template, aluno=aluno, url_base="static")

    return html(Markup(card))


def html(card_blog):
    template = """
        
    <!DOCTYPE html>
    <!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
    <!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
    <!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
        <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Charity &mdash; 100% Free Fully Responsive HTML5 Template by FREEHTML5.co</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="Free HTML5 Template by FREEHTML5.CO" />
        <meta name="keywords" content="free html5, free template, free bootstrap, html5, css3, mobile first, responsive" />
        <meta name="author" content="FREEHTML5.CO" />
    
      <!-- 
        //////////////////////////////////////////////////////
    
        FREE HTML5 TEMPLATE 
        DESIGNED & DEVELOPED by FREEHTML5.CO
            
        Website: 		http://freehtml5.co/
        Email: 			info@freehtml5.co
        Twitter: 		http://twitter.com/fh5co
        Facebook: 		https://www.facebook.com/fh5co
    
        //////////////////////////////////////////////////////
         -->
    
        <!-- Facebook and Twitter integration -->
        <meta property="og:title" content=""/>
        <meta property="og:image" content=""/>
        <meta property="og:url" content=""/>
        <meta property="og:site_name" content=""/>
        <meta property="og:description" content=""/>
        <meta name="twitter:title" content="" />
        <meta name="twitter:image" content="" />
        <meta name="twitter:url" content="" />
        <meta name="twitter:card" content="" />
    
        <!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
        <link rel="shortcut icon" href="favicon.ico">
    
        <!-- <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,700,300' rel='stylesheet' type='text/css'> -->
        
        <!-- Animate.css -->
        <link rel="stylesheet" href="{{ url_base }}/css/animate.css">
        <!-- Icomoon Icon Fonts-->
        <link rel="stylesheet" href="{{ url_base }}/css/icomoon.css">
        <!-- Bootstrap  -->
        <link rel="stylesheet" href="{{ url_base }}/css/bootstrap.css">
        <!-- Superfish -->
        <link rel="stylesheet" href="{{ url_base }}/css/superfish.css">
    
        <link rel="stylesheet" href="{{ url_base }}/css/style.css">
    
    
        <!-- Modernizr JS -->
        <script src="{{ url_base }}/js/modernizr-2.6.2.min.js"></script>
        <!-- FOR IE9 below -->
        <!--[if lt IE 9]>
        <script src="{{ url_base }}/js/respond.min.js"></script>
        <![endif]-->
    
        </head>
        <body>
            <div id="fh5co-wrapper">
            <div id="fh5co-page">
            <div class="header-top">
                <div class="container">
                    <div class="row">
                        <div class="col-md-6 col-sm-6 text-left fh5co-link">
                            <a href="#">FAQ</a>
                            <a href="#">Forum</a>
                            <a href="#">Contact</a>
                        </div>
                        <div class="col-md-6 col-sm-6 text-right fh5co-social">
                            <a href="#" class="grow"><i class="icon-facebook2"></i></a>
                            <a href="#" class="grow"><i class="icon-twitter2"></i></a>
                            <a href="#" class="grow"><i class="icon-instagram2"></i></a>
                        </div>
                    </div>
                </div>
            </div>
            <header id="fh5co-header-section" class="sticky-banner">
                <div class="container">
                    <div class="nav-header">
                        <a href="#" class="js-fh5co-nav-toggle fh5co-nav-toggle dark"><i></i></a>
                        <h1 id="fh5co-logo"><a href="index.html">Charity</a></h1>
                        <!-- START #fh5co-menu-wrap -->
                        <nav id="fh5co-menu-wrap" role="navigation">
                            <ul class="sf-menu" id="fh5co-primary-menu">
                                <li>
                                    <a href="index.html">Home</a>
                                </li>
                                <li>
                                    <a href="#" class="fh5co-sub-ddown">Get Involved</a>
                                    <ul class="fh5co-sub-menu">
                                        <li><a href="#">Donate</a></li>
                                        <li><a href="#">Fundraise</a></li>
                                        <li><a href="#">Campaign</a></li>
                                        <li><a href="#">Philantrophy</a></li>
                                        <li><a href="#">Volunteer</a></li>
                                    </ul>
                                </li>
                                <li>
                                    <a href="#" class="fh5co-sub-ddown">Projects</a>
                                     <ul class="fh5co-sub-menu">
                                        <li><a href="#">Water World</a></li>
                                        <li><a href="#">Cloth Giving</a></li>
                                        <li><a href="#">Medical Mission</a></li>
                                    </ul>
                                </li>
                                <li><a href="about.html">About</a></li>
                                <li class="active"><a href="blog.html">Blog</a></li>
                                <li><a href="contact.html">Contact</a></li>
                            </ul>
                        </nav>
                    </div>
                </div>
            </header>
            
            
    
            <div class="fh5co-hero">
                <div class="fh5co-overlay"></div>
                <div class="fh5co-cover text-center" data-stellar-background-ratio="0.5" style="background-image: url({{ url_base }}/images/cover_bg_1.jpg);">
                    <div class="desc animate-box">
                        <h2>Our <strong>Blog &amp; News</strong></h2>
                        <span>HandCrafted by <a href="http://frehtml5.co/" target="_blank" class="fh5co-site-name">FreeHTML5.co</a></span>
                        <span><a class="btn btn-primary btn-lg" href="#">Donate Now</a></span>
                    </div>
                </div>
    
            </div>
            
            <div id="fh5co-blog-section" class="fh5co-section-gray">
                <div class="container">
                    <div class="row">
                        <div class="col-md-8 col-md-offset-2 text-center heading-section animate-box">
                            <h3>Read. Learn. Share</h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Velit est facilis maiores, perspiciatis accusamus asperiores sint consequuntur debitis.</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="row row-bottom-padded-md">
                        {{ card_blog }}
    
                    <div class="row">
                        <div class="col-md-4 col-md-offset-4 text-center animate-box">
                            <a href="#" class="btn btn-primary btn-lg">Our Blog</a>
                        </div>
                    </div>
    
                </div>
            </div>
            <!-- fh5co-blog-section -->
    
            
            <footer>
                <div id="footer">
                    <div class="container">
                        <div class="row">
                            <div class="col-md-6 col-md-offset-3 text-center">
                                <p class="fh5co-social-icons">
                                    <a href="#"><i class="icon-twitter2"></i></a>
                                    <a href="#"><i class="icon-facebook2"></i></a>
                                    <a href="#"><i class="icon-instagram"></i></a>
                                    <a href="#"><i class="icon-dribbble2"></i></a>
                                    <a href="#"><i class="icon-youtube"></i></a>
                                </p>
                                <p>Copyright 2016 Free Html5 <a href="#">Charity</a>. All Rights Reserved. <br>Made with <i class="icon-heart3"></i> by <a href="http://freehtml5.co/" target="_blank">Freehtml5.co</a> / Demo Images: <a href="https://unsplash.com/" target="_blank">Unsplash</a></p>
                            </div>
                        </div>
                    </div>
                </div>
            </footer>
        
    
        </div>
        <!-- END fh5co-page -->
    
        </div>
        <!-- END fh5co-wrapper -->
    
        <!-- jQuery -->
    
    
        <script src="{{ url_base }}/js/jquery.min.js"></script>
        <!-- jQuery Easing -->
        <script src="{{ url_base }}/js/jquery.easing.1.3.js"></script>
        <!-- Bootstrap -->
        <script src="{{ url_base }}/js/bootstrap.min.js"></script>
        <!-- Waypoints -->
        <script src="{{ url_base }}/js/jquery.waypoints.min.js"></script>
        <script src="{{ url_base }}/js/sticky.js"></script>
    
        <!-- Stellar -->
        <script src="{{ url_base }}/js/jquery.stellar.min.js"></script>
        <!-- Superfish -->
        <script src="{{ url_base }}/js/hoverIntent.js"></script>
        <script src="{{ url_base }}/js/superfish.js"></script>
        
        <!-- Main JS -->
        <script src="{{ url_base }}/js/main.js"></script>
    
        </body>
    </html>


    """

    return render_template_string(template, url_base="static", card_blog=card_blog)


if __name__ == "__main__":
    app.run(debug=True)
