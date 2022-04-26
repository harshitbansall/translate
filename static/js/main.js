function Login() {
    $("#loaderFrame").show();
    $.ajax({
        type: "POST",
        url: "/auth/login",
        data: {
            username: $("#usernameInputBox").val(),
            password: $("#passwordInputBox").val(),
        },
        error: function (object, status) {
            if (object.status === 400) {
                $("#loaderFrame").hide();
                alert("Error");
            }
        },
        success: function (result) {
            $("#loaderFrame").hide();
            alert(result);
            window.location.replace("/home");
        }
    });
}
function SignUp() {
    $("#loaderFrame").show();
    $.ajax({
        type: "POST",
        url: "/auth/signup",
        data: {
            full_name: $("#firstNameField").val() + " " + $("#lastNameField").val(),
            username: $("#usernameField").val(),
            password: $("#passwordField").val(),
            email: $("#emailField").val(),
        },
        error: function (object, status) {
            if (object.status === 400) {
                $("#loaderFrame").hide();
                alert("Error");
            }
        },
        success: function (result) {
            $.ajax({
                type: "POST",
                url: "/auth/login",
                data: {
                    username: $("#usernameField").val(),
                    password: $("#passwordField").val(),
                },
                success: function (result) {
                    $("#loaderFrame").hide();
                    alert(result);
                    window.location.replace("/home");
                }
            });
        }
    });

}
function Logout() {
    $.ajax({
        type: "POST",
        url: "/auth/logout",
        headers: { "Authorization": "JWT " + accessToken },
        success: function (result) {
            alert(result);
            window.location.replace("/home");
        }
    });
}

function GoToSignUp() {
    window.location.replace("/signup" + window.location.search);
}

function SaveSentence(counter, sentence_id, target_lang) {
    $.ajax({
        type: "POST",
        url: "/saveSentence",
        headers: { "Authorization": "JWT " + accessToken },
        data: {
            sentence_id:sentence_id,
            translated_sentence: $("#transliteration"+counter).val(),
            target_lang: target_lang,
        },
        error: function (xhr, status) {
            if (xhr.status === 401) {
                alert("Login Required.");
            }
        },
        success: function (result) {
            alert(result);
        }
    });
}

function EnterEventLogin() {
    if (event.key === 'Enter') {
        Login();
    }
}