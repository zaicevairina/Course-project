from peewee import *
from models import Department, Branch, Project, Supplier, Purchase, Equipment

if __name__ == '__main__':

	department1 = Department.create(title='продуктовый', director='Трескова')
	department2 = Department.create(title='цветочный', director='Зайцева')
	department3 = Department.create(title='промышленный', director='Витько')
	department4 = Department.create(title='обувной', director='Шитова')
	department5 = Department.create(title='мебельный', director='Полякова')

	branch1 = Branch.create(address='Москва')
	branch2 = Branch.create(address='Саратов')
	branch3 = Branch.create(address='Самара')

	supplier1 = Supplier.create(organization='корова', requisites=111)
	supplier2 = Supplier.create(organization='поле', requisites=222)
	supplier3 = Supplier.create(organization='фабрика', requisites=333)
	supplier4 = Supplier.create(organization='сад', requisites=444)
	supplier5 = Supplier.create(organization='завод', requisites=555)
	supplier6 = Supplier.create(organization='сапожник', requisites=666)
	supplier7 = Supplier.create(organization='кондитер', requisites=777)


	project1 = Project.create(title='Малыш', budget='1000')
	project2 = Project.create(title='Сластена', budget='2000')
	project3 = Project.create(title='Цветочки', budget='1500')
	project4 = Project.create(title='Стройка', budget='2500')
	project5 = Project.create(title='Обуть', budget='500')

	equipment1 = Equipment.create(name='коробка', project=project1)
	equipment2 = Equipment.create(name='фольга', project=project2)
	equipment3 = Equipment.create(name='шило', project=project5)
	equipment4 = Equipment.create(name='молоток', project=project4)
	equipment5 = Equipment.create(name='пила', project=project4)
	equipment6 = Equipment.create(name='лейка', project=project3)
	equipment7 = Equipment.create(name='грабли', project=project3)
	equipment8 = Equipment.create(name='фольга', project=project5)

	purchase1 = Purchase.create(good='молоко',amount=10, supplier=supplier1, project=project1, department=department1, branch=branch1)
	purchase2 = Purchase.create(good='каша',amount=25, supplier=supplier2, project=project1, department=department1, branch=branch1)
	purchase3 = Purchase.create(good='конфеты',amount=100, supplier=supplier7, project=project2, department=department1, branch=branch1)
	purchase4 = Purchase.create(good='розы',amount=50, supplier=supplier4, project=project3, department=department2, branch=branch2)
	purchase5 = Purchase.create(good='ромашки',amount=20, supplier=supplier4, project=project3, department=department2, branch=branch2)
	purchase6 = Purchase.create(good='станок1',amount=1, supplier=supplier5, project=project4, department=department3, branch=branch1)
	purchase7 = Purchase.create(good='станок2',amount=4, supplier=supplier5, project=project4, department=department3, branch=branch1)
	purchase8 = Purchase.create(good='станок3',amount=2, supplier=supplier5, project=project4, department=department3, branch=branch1)
	purchase9 = Purchase.create(good='сапоги',amount=1, supplier=supplier6, project=project5, department=department4, branch=branch1)
	purchase10 = Purchase.create(good='туфли',amount=6, supplier=supplier6, project=project5, department=department4, branch=branch1)
	purchase11 = Purchase.create(good='стол',amount=1, supplier=supplier3, project=project4, department=department5, branch=branch3)
	purchase12 = Purchase.create(good='стул',amount=5, supplier=supplier3, project=project4, department=department5, branch=branch3)
	purchase12 = Purchase.create(good='стол',amount=5, supplier=supplier3, project=project3, department=department2, branch=branch3)





