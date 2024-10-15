

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

function quantite_ajour(id_article)
{
    let quantite = parseInt(document.getElementById(`quantite-${id_article}`).value);

    let csrftoken = get_csrf_token();

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
        location.reload();
        if (data.success)
        {
            
            console.log('mis a jour avec success');
        }
        else 
        {
            console.log(' erreur du  mis a jour ');
        }
    } )
    .catch(error => console.error('Erreur:', error ));
   

}

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
        //location.reload();
        if (data.success === true )
        {
            location.reload();
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
            location.reload();
            console.log(' erreur du  mis a jour ');
            document.getElementById("message").innerText = "Erreur lors de l’ajout de l'article.";
        }
    } )
    .catch(error => console.error('erreur:', error ));
    
}



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

function change_value(id_article)
{
    let quantite = parseInt(document.getElementById(`quantite-${id_article}`).value);
    //console.log(quantite)

    
}