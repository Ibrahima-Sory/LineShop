
        //fonction pour changer la quatité et calculer le total uniquement en front
function total_quantité()
{
    //let prixTotal = document.getElementById("prixTotal").textContent;
    let prixTotal = 0 ;
  

    document.querySelectorAll(".articles").forEach(
        function(item) {

            
            let quantite = item.querySelector(".quantite").value ; 
            console.log(quantite);
            //quantite = parseInt(quantite);
            //console.log(quantite);
            let prix = item.querySelector(".quantite").getAttribute("data-prix");
            console.log(prix);

            total = quantite * prix ;
            console.log( "total article:" + total) 

            prixTotal += total
        
        }
    );

   // let articles = document.querySelectorAll(".articles")
   // console.log(articles)
   // let quantite = 1 ;
   // quantite = document.querySelector(".quantite").value ; 
    //quantite = parseInt(quantite)
    //console.log(quantite);
    

    //let article = document.getElementById(`quantite-${id_article}`);;
   // console.log(article)
    //let quantite = parseInt(article.value )
   // console.log(quantite)
    //quantite = quantite ;
    //console.log(quantite);
    document.getElementById("prixTotal").textContent= prixTotal ;

    console.log("Total Panier:" +prixTotal)



}

//Fonction pour la validation du panier 

function validerPanier() {
    quantite_ajour()

    let csrftoken = get_csrf_token();

    fetch("/panier/valider/", 
        {   
            method: 'POST',
            headers: {
                'Content-Type': "application/json",
                'X-CSRFToken': csrftoken
            }
        }
    )
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            //alert('Panier validé avec succès. Total: ' + data.totalPanier + ' FG');
            // Rediriger vers la page de confirmation d'achat, par exemple
            //window.location.href = `/commande/confirmation/${data.achat_id}/`;
            window.location.href = `/panier/valider/commmande/${data.achat_id}`;
        } else {
            // Afficher les erreurs si elles existent
            alert('Erreur lors de la validation du panier ' );
        }
    })
    .catch(error => console.error('Erreur:', error));
}







//------------------------------------------------------------------------------------------------

// fonction change de quantite avec des buttons
function change_quantite(ordre , id_article)
{ 
    //console.log(id_article);
    let input = document.getElementById(`quantite-${id_article}`);
    //console.log(input); 
    let quantite = parseInt(input.value); 

    if(ordre== 'incrementation')
    {
        quantite++;
    }
    else if(ordre== 'decrementation' && quantite > 1)
    {
        quantite--;
    }
    //console.log(quantite)
    input.value=quantite;

    quantite_ajour(id_article);
    //console.log("ordre:"+ ordre + "article ID:"+ id_article );
}   
//---------------------------------fin---------------------------------------


//fonction pour mettre a jour la quantité d'un article dans la base de donnée 
function quantite_ajour()
{
    //let quantite = parseInt(document.getElementById(`quantite-${id_article}`).value);

    let csrftoken = get_csrf_token();

    let prixTotal = 0 ;
  

    document.querySelectorAll(".articles").forEach(
        function(item) {

            
            let quantite = item.querySelector(".quantite").value ; 
            console.log(quantite);
            quantite = parseInt(quantite);
            //console.log(quantite);
            let id_article = item.querySelector(".quantite").getAttribute("data-id");

            fetch("/panier/change_quantite/", 
                {   
                    method:'POST',
        
                    headers:{
                        'Content-Type':"application/json",
                        'X-CSRFToken': csrftoken 
        
        
                    },
        
                    body: JSON.stringify({
                            "article_id":id_article,
                            "quantite":quantite   
                    })         
                               
        
                }    
                  
            )
            .then(response => response.json())
            .then(data => {
                //location.reload();
                if (data.success)
                {
                    document.getElementById('prixTotal').textContent = data.prixTotal ;
                    console.log('mis a jour avec success');
        
                }
                else 
                {
                    console.log(' erreur du  mis a jour ');
                }
            } )
            .catch(error => console.error('Erreur:', error ));
           
        
        }
        
        
    );

    
   

}
//----------------------------fin---------------------------------------------

//fonction qui gère les tokens 
function get_csrf_token()
{
    const token = document.querySelector('meta[name="csrf-token"] ').getAttribute('content');
    return token ;
}

function change_quantite_achat(ordre , id_article)
{ 
    //console.log(id_article);
    let input = document.getElementById(`quantite-${id_article}`);
    //console.log(input); 
    let quantite = parseInt(input.value); 

    if(ordre== 'incrementation')
    {
        quantite++;
    }
    else if(ordre== 'decrementation' && quantite > 1)
    {
        quantite--;
    }
    //console.log(quantite)
    input.value=quantite;

    //ajouter_quantite(id_article);
    //console.log("ordre:"+ ordre + "article ID:"+ id_article );
    //quantite_achat(id_article);

}

              //-- ajout d'un article au panier avec la quatité 
function ajouter_quantite(id_article)
{
    let quantite = parseInt(document.getElementById(`quantite-${id_article}`).value);
    //console.log(quantite)
    let csrftoken = get_csrf_token();


    fetch(`/add/${id_article}/`, 
        {   
            method:'POST',

            headers:{
                'Content-Type':"application/json",
                'X-CSRFToken': csrftoken 


            },

            body: JSON.stringify({
                    "article_id":id_article,
                    "quantite":quantite   
            })         
                       

        }    
          
    )
 .then(response => response.json())
        
        
    .then(data => {
        location.reload();
        if (data.success === true )
        {
            //location.reload();
            console.log('mis a jour avec success');
            //document.getElementById("message").innerText = "Article ajouté avec succès !";
        }

        if (data.success === false )
            {
                //location.reload() 
                console.log("redirection") 
                window.location.href = '/accountsconnexion/';
                return null ; 
            }

        else 
        {
            //location.reload();
            console.log(' erreur du  mis a jour ');
            document.getElementById("message").innerText = "Erreur lors de l’ajout de l'article.";
        }
    } )
    .catch(error => console.error('erreur:', error ));
    
}


        // fonction pour l'affichage des messages 
setTimeout(function() {
    let message = document.getElementById('messageS');
    if(message)
    {
        message.style.transition = "opacity 0.5s ease-out";
        message.style.opacity = "0"; // Déclenche l'effet de fade-out
        
        // Supprimer complètement l'élément après l'effet de disparition
        setTimeout(
            function() {
                message.remove();
            }, 500 ); // 500 ms pour l'effet de transition
        
        
    }

}, 3000); // 500 ms pour l'effet de transition


// --------------------------------------------------------------------------------------------
                // fonction-non utilisée pour l'ajout recuperer un article pour un achat 
function quantite_achat(id_article)
{
    let quantite = parseInt(document.getElementById(`quantite-${id_article}`).value);
    //console.log(quantite)
    let csrftoken = get_csrf_token();


    fetch(`/achat/${id_article}/`, 
        {   
            method:'POST',

            headers:{
                'Content-Type':"application/json",
                'X-CSRFToken': csrftoken 


            },

            body: JSON.stringify({
                    "article_id":id_article,
                    "quantite":quantite   
            })         
                       

        }    
          
    )
    .then(response => response.json())
    .then(data => {
        //location.reload();
        //console.log('Réponse JSON:', data); 
        if (data.success)
        {
            console.log('Réponse JSON:', data);
            console.log('mis a jour avec success');
            //document.getElementById("message").innerText = "Article ajouté avec succès !";



        }
        else 
        {
            console.log(' erreur du  mis a jour ');
            document.getElementById("message").innerText = "Erreur lors de l’ajout de l'article.";
        }
    } )
    .catch(error => console.error('Erreur:', error ));

}

