# miniscience-4sem
## lab01
Работа с сетками с использованием библиотеки gmsh.
### 1 stage
Построение полого внутри тора. 

**Содержание папки:**
1. "1.1 thor.py" - код;
2. "1. thor.png" - скриншот.

### 2 stage
Построение сетки из готового stl-файла.

**Содержание папки:**
1. "2. griffin.stl" - исходная модель;
2. "2.1 stl-file.py" - код;
3. 4 скриншота.

## lab02
Визуализация данных с помощью VTK и Paraview.
Используя модель прошлой лабы, были смоделированы скалярное поле (бегущая вверх волна) и векторное поле (задавалась скорость точек, в результате гриффин машет крыльями).

**Содержание папки:**
1. "griffin.stl" - исходная модель;
2. "main.py" - код;
3. "video links.txt" - текстовый файл с ссылками на видео на YouTube-е с резульатами моделирования.

## lab03
Использование стороннего солвера для расчетов на примере FEniCS.
Была разобрана задача с линейной упругостью в 3D. В результате смоделировано провисание провода между двумя опорами. По сравнению со стартовым примером изменена геометрия объекта (цилиндр вместо параллелепипеда) и добавлено граничное условие на оба конца объекта (неподвижность точек).

**Содержание папки:**
1. "elasticity-cable.py" - код;
2. "elasticity-cable" - папка с данными расчета и двуми скриншотами "scrin-front.png" и "scrin-side.png".

## microproject
Здесь собраны некоторые части, необходимые для моделирования поведения ветрогенератора в потоке ветра.

### Часть 1
**Работа с сетками.** В этой части создается сетка лопасти ветрогенератора из stl-файла с помощью gmsh и сохранется в msh-файл. Стоит отметить, что исходная stl-модель является тонкостенной, а в процессе создания сетки, объект становится полностью заполненым. Затем с помощью библиотеки meshio сетка из формата .msh в формат .xdmf. Далее этот файл используется для создания расчетной сетки в FEniCS.

### Часть 2
**3D обтекание.** Здесь создается прямоугольная область с полостью в форме сферы средствами FEniCS. Затем адаптируется код из примера FEniCS с обтеканием цилиндра в 2D для обтекания шара в 3D. Меняются геометрия, граничные условия и все векторы становятся с тремя компонентами.

**Содержание папки:**
1. "stl-file.py" - создание сетки из stl в msh
2. "remash.py" - конвертация msh в xdmf
3. "blade.py" - включение геометрии в FEniCS
4. "mesh_box_sphere.py" - создание 3D сетки с полостью
5. "navier_stokes_cylinder_3d.py" - расчет обтекания сферы
6. "video-link.txt" - ссылка на видео с обтеканием
7. "wind_turbine_blade" - директория, содержащая stl файл лопасти

## microproject
Представлена одна из версий макропроекта, созданного совместно с Герасимовым Ильей (gerasimov.ia@phystech.edu) и Матвеичевым Андреем (matveichev.ap@phystech.edu).
Суть макропроекта заключается в следующем: моделирование хода лучей в атмосфере планеты. Подробнее смотри файл "macroproject.pdf"
