// Adds a comment in the petDetail page
$(document).ready(function () {
    var $buttonLang = $("#changeLan")
    $buttonLang.click(function(event){
      event.preventDefault();
      var $endpoint = window.location.origin + "/resume/" || window.location.href
      var $language = $buttonLang.val();
      
      $.ajax({
        method: "GET",
        url: $endpoint,
        data: {"language": $language},
        success: handleFormSuccess,
        error: handleFormError,
      })
      function handleFormSuccess(data, textStatus, jqXHR){
        console.log(data)
        console.log(textStatus)
        console.log(jqXHR)
        
        // var successMessage = $(`<div class="alert alert-success fade show" role="alert">
        //                           Message sent
        //                         <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        //                           <span aria-hidden="true">&times;</span>
        //                         </button>
        //                         </div>`)
        // $("#commentPet").remove();
        // $(".special-width").prepend($(successMessage));
        console.log(data)
        $buttonLang.val("E");
      }
      function handleFormError(data, textStatus, errorThrown){
        console.log(data)
        console.log(textStatus)
        console.log(errorThrown)
      }
    })
   }
  )