const forms = document.querySelectorAll(".like-form")
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value 

forms.forEach((form) => {
  form.addEventListener("submit", (event) => {
    event.preventDefault()
    const postId = event.target.dataset.postId
    axios({
      method: 'post',
      url: `/posts/${postId}/like/`,   // 앞에 슬래시를 붙이지 않으면 이전 url에 더해지는 방식으로 작동한다
      headers: {'X-CSRFToken': csrftoken},
      data: {
        like: event.submitter.value,
      },
    }).then((response) => {
        if (response.data.logged_in === false) {
          window.location = '/accounts/login/'
        } else {
          const isLiked = response.data.isLiked
          const likeBtn = document.querySelector(`#like-${postId}`)
          const imgTag = likeBtn.querySelector('img')

          if (isLiked === true) {
            imgTag.src = "/static/like.png"
            imgTag.alt = "like"
          } else if (isLiked === false) {
            imgTag.src = "/static/unlike.png"
            imgTag.alt = "unlike";
          }
        }
      }).catch((error) => {
        console.log(error.response)
      })
    })
  })