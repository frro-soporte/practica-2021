"""Magic Methods"""

from __future__ import annotations
from typing import List


# NO MODIFICAR - INICIO
class Article:
    """Agregar los métodos que sean necesarios para que los test funcionen.
    Hint: los métodos necesarios son todos magic methods
    Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization
    """

    def __init__(self, name: str) -> None:
        self.name = name

    # NO MODIFICAR - FIN

    # Completar
    def hola():
        return "hola"

    def __str__(self) -> str:
        return self.name.capitalize()

    def __repr__(self) -> str:
        return f'Article("{self.name}")'

    def __eq__(self, other: object) -> bool:
        pass
        if(type(self) != type(other)):
            return False
        else:
            return self.name == other.name

    def __lt__(self, other: Article) -> bool:
        return self.name < other.name


# NO MODIFICAR - INICIO
class ShoppingCart:
    """Agregar los métodos que sean necesarios para que los test funcionen.
    Hint: los métodos necesarios son todos magic methods
    Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization
    """

    def __init__(self, articles: List[Article] = None) -> None:
        if articles is None:
            self.articles = []
        else:
            self.articles = articles

    def add(self, article: Article) -> ShoppingCart:
        self.articles.append(article)
        return self

    def remove(self, remove_article: Article) -> ShoppingCart:
        new_articles = []

        for article in self.articles:
            if article != remove_article:
                new_articles.append(article)

        self.articles = new_articles

        return self

    # NO MODIFICAR - FIN

    # Completar

    def __str__(self) -> str:
        articles_str = []
        for a in self.articles:
            articles_str.append(str(a))
        return str(articles_str)

    def __repr__(self) -> str:
        return f"ShoppingCart({self.articles})"

    def __eq__(self, other: object) -> bool:
        if (type(self) != type(other)):
            return False
        else:
            for i,a in enumerate(sorted(self.articles)):
                if a != sorted(other.articles)[i]:
                    return False
            return True

    def __add__(self, other: ShoppingCart) -> ShoppingCart:
        add_list = self.articles.extend(other.articles)
        return ShoppingCart(add_list)

# NO MODIFICAR - INICIO

manzana = Article("Manzana")
pera = Article("Pera")
tv = Article("Television")

# Test de conversión a String
assert str(ShoppingCart().add(manzana).add(pera)) == "['Manzana', 'Pera']"

# Test de reproducibilidad
carrito = ShoppingCart().add(manzana).add(pera)
assert carrito == eval(repr(carrito))

# Test de igualdad
assert ShoppingCart().add(manzana) == ShoppingCart().add(manzana)

# Test de remover objeto
assert ShoppingCart().add(tv).add(pera).remove(tv) == ShoppingCart().add(pera)

# Test de igualdad con distinto orden
assert ShoppingCart().add(tv).add(pera) == ShoppingCart().add(pera).add(tv)

# Test de suma
combinado = ShoppingCart().add(manzana) + ShoppingCart().add(pera)
assert combinado == ShoppingCart().add(manzana).add(pera)

# NO MODIFICAR - FIN
