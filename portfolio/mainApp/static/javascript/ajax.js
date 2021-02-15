// Adds a comment in the petDetail page
$(document).ready(function () {
    alert("d");
    var $myForm = $("#changeLan")
    $myForm.submit(function(event){
      event.preventDefault();
      var $formData = $(this).serialize();
      var $endpoint = window.location.origin + $myForm.attr("data-url") || window.location.href
        
      $.ajax({
        method: "POST",
        url: $endpoint,
        data: $formData,
        success: handleFormSuccess,
        error: handleFormError,
      })
      function handleFormSuccess(data, textStatus, jqXHR){
        console.log(data)
        console.log(textStatus)
        console.log(jqXHR)
        
        var successMessage = $(`<div class="alert alert-success fade show" role="alert">
                                  Message sent
                                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                  <span aria-hidden="true">&times;</span>
                                </button>
                                </div>`)
        $("#commentPet").remove();
        $(".special-width").prepend($(successMessage));
      }
      function handleFormError(data, textStatus, errorThrown){
        console.log(data)
        console.log(textStatus)
        console.log(errorThrown)
      }
    })
   }
  )