
// $(document).ready(function() {
    
// });

function WelcomeMsg(){
    alert("Selamat Datang!")
}

// form validate
function validate() {
    if(document.myForm.isPaid.checked == false){
        alert("Pastikan menyemak kotak untuk memastikan anda telah membayar")
        return false;
    }

    if(document.myForm.Nama.value == ""){
        alert("Please provide your name!")
        document.myForm.Nama.focus();
        return false;
    }
    else if( document.myForm.Email.value == ""){
        alert("Please provide your email!")
        document.myForm.Email.focus();
        return false;
    }
    else if( document.myForm.Telefon.value == "" || isNaN( document.myForm.Telefon.value) || document.myForm.Telefon.value.length < 10){
        alert("Please provide a phone on the format (XXX)XXX XXXX.")
        document.myForm.Telefon.focus();
        return false;
    }
    else if( document.myForm.Message.value == ""){
        alert("Please provide message!")
        document.myForm.Message.focus();
        return false;
    }
    alert("Submitted successfully.")

    return (true);
}

// form validate
function validatePercuma() {
    if(document.myForm.Nama.value == ""){
        alert("Please provide your name!")
        document.myForm.Nama.focus();
        return false;
    }
    else if( document.myForm.Email.value == ""){
        alert("Please provide your email!")
        document.myForm.Email.focus();
        return false;
    }
    alert("Berjaya! Anda akan mendapat khabar kami dari email tidak lama lagi.")

    return (true);
}

//onMouseOver
function MouseOver(x) {
    x.style.width = "100%";
}
//onMouseOut
function MouseOut(x) {
    x.style.width = "80%";
}

