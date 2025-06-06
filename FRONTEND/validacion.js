window.onload = function() {

    const token = localStorage.getItem("token");
    const userCorreo = localStorage.getItem("userCorreo");

    if (token) {
        
        document.getElementById('agendar-link').style.display = 'inline-block';
        document.getElementById('configurar-link').style.display = 'inline-block';
        return;
    }else{
        alert("Debes iniciar sesión para que puedas agendar");
         return;
    }
}