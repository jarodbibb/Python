
            $(document).ready(function(){
                
            $('button').click(function(){
                    if(this.id === "blue"){
                      $('h2').html("Leonardo");
                       $('img').attr("src","/static/leonardo.jpg")
                        
                    }
                  if(this.id ==="purple"){
                      $('h2').html("Donaldtello");
                      $('img').attr("src","/static/donatello.jpg")
                  }
                  if(this.id === "orange"){
                      $('h2').html("Michelangelo");
                      $('img').attr("src", "/static/michelangelo.jpg")
                  }
                  if(this.id === "red"){
                      $('h2').html("Raphael");
                      $('img').attr("src", "/static/raphael.jpg")
                  }
                
                  
                })
                       $('#april').submit( ()=> {
                           $('img').attr("src", "/static/notapril.jpg")
                           return false
                       })
            })