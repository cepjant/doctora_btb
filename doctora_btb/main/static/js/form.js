
var servResponse = document.querySelector('#response');

document.forms.fb_form.onsubmit = function(e) {

    e.preventDefault();


    var xhr = new XMLHttpRequest();

    xhr.open('POST', 'send_message/');
    var data = $('form').serialize()

    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    xhr.onreadystatechange = function() {

    if(xhr.readyState === 4 && xhr.status === 200) {


        form = document.forms.fb_form;


        if(xhr.responseText === "OK") {

          form.reset();
          document.getElementById("fb_btn").innerHTML = "Сообщение отправлено";
        }

        else if(xhr.responseText === "email") {
          document.getElementById("fb_btn").innerHTML = 'Введите правильный адрес электронной почты';
        }
        else if(xhr.responseText === "body") {
          document.getElementById("fb_btn").innerHTML = 'Недопустимое содержание в поле "сообщение"';
        }
        else if(xhr.responseText === "name") {
          document.getElementById("fb_btn").innerHTML = 'Недопустимое содержание в поле "имя"';
        }
        else if(xhr.responseText === "CAPTCHA") {
          document.getElementById("fb_btn").innerHTML = 'Подтвердите, что вы не робот.';
        }
        else {
          document.getElementById("fb_btn").innerHTML = 'Ошибка.';
        }


    }

}

    xhr.send(data);

};
