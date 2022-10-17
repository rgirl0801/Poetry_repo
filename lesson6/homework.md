7.1. Найдите кпопку c текстом "Gold". Попробуйте подобрать как минимум 2 разных XPATH и/или CSS-селекторов
http://suninjuly.github.io/xpath_examples

div:nth-child(2)>button:nth-child(3)

//text()[. = 'Gold']

//button[contains(text(), 'Gold')]

7.2. Найдите элемент с текстом "Lenin cat". Чем больше разных XPATH и/или CSS-селекторов сможете подобрать, тем лучше
http://suninjuly.github.io/cats.html

//p[contains(text(), "Lenin cat")]
#politic
.lenin-cat
[name="Vova"]
[data-name="Vladimir"]