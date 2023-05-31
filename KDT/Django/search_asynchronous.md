# 검색 비동기 구현

<br/>

### html
- ```html
    <form id='markets--index--search--block' class='d-none'>
      <input name='q' type="search">

      <button type='submit'>
        <i class="bi bi-search"></i>
      </button>
    </form>

    <section class='markets--index--section'>
      {% for post in posts %}
        <h1>{{ post.title }}</h1>
      {% endfor %}
    </section>
  ```

<br/>

### JS
- ```javascript
    const postsContainer = document.querySelector('.markets--index--section')
    const searchForm = document.querySelector('#markets--index--search--block')
    const searchInput = document.querySelector('#markets--index--search--block > input')

    searchInput.addEventListener('input', async (event) => {
      const searchValue = event.target.value
      const urlParams = new URLSearchParams(window.location.search)
      const disValue = urlParams.get('dis')
      const categoryValue = urlParams.get('category')

      try {
        const response = await fetch(
          `/markets/?dis=${disValue}&category=${categoryValue}&q=${searchValue}`
        )

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const html = await response.text()
        const parser = new DOMParser()
        const doc = parser.parseFromString(html, 'text/html')
        const posts = doc.querySelector('.markets--index--section')

        if (searchValue) {
          const regex = new RegExp(searchValue, 'gi')
          const h1Elements = posts.querySelectorAll('h1')
          h1Elements.forEach((h1) => {
            const originalContent = h1.innerHTML
            const highlightedContent = originalContent.replace(regex, (match) => `<span class="markets--index--highlight">${match}</span>`)
            h1.innerHTML = highlightedContent
          })
        }

        postsContainer.innerHTML = posts.innerHTML
      } catch (error) {
        console.error(error)
      }
    })
  ```

<br/>

### views.py
- ```python
    def index(request):
      dis = request.GET.get('dis')
      category = request.GET.get('category')
      q = request.GET.get('q')

      if dis == 'town':
          posts = Post.objects.filter(user__town=request.user.town)
      else:
          posts = Post.objects.filter(user__building=request.user.building)

      if category == 'used':
          posts = posts.filter(price__gt=0)
      elif category == 'free':
          posts = posts.filter(price=0)
      
      if q:
          posts = posts.filter(title__icontains=q)

      posts = posts.order_by('-pk')

      context = {'posts': posts}
      return render(request, 'markets/index.html', context)
  ```