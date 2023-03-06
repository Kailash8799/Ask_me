function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
  function doLikes(id) { 
    let csrftoken = getCookie("csrftoken");
    fetch("/question_ans/likequestion/", {
      method: "post",
      body: JSON.stringify({
        id: id,
      }),
      headers: {
        Accept: "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    })
      .then((res) => {
        return res.json();
      })
      .then((i) => {
        document.getElementById(id+"like").remove();
        document.getElementById("likebtn").innerHTML = `<div class="mt-4">
        <button
              class="inline-flex items-center p-2 text-sm font-medium text-center text-gray-400 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-50"
              type="button">
              <i class="fa-solid fa-thumbs-up"></i>
            </button>
      </div>`;
      });
  }
  