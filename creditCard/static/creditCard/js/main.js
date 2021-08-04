$("#submit").click(function(){
  var formState = form.checkValidity();
  if (formState) {
    $(this).html(
      '<span id="loader" class="spinner-grow spinner-grow-sm me-2" role="status" aria-hidden="true"></span>Chargement...'
    );
  } else {
      alert('Veuillez remplir le formulaire !');
    // console.log($this.html);
    // $("#loader").addClass("");
  }
});
