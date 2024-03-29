# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

my_str = 'Погода — совокупность значений метеорологических элементов и атмосферных явлений, наблюдаемых в определённый момент времени в той или иной точке пространства. ' \
    'Понятие Погода относится к текущему состоянию атмосферы, в противоположность понятию «Климат», которое относится к среднему состоянию атмосферы за длительный ' \
    'период времени. Если нет уточнений, то под термином Погода понимают погоду на Земле. Погодные явления протекают в тропосфере (нижней части атмосферы) и в стратосфере '\
    '— атмосферном слое, располагающемся на высоте примерно от 11 до 50 километров. Погоду можно описать давлением, температурой и влажностью воздуха, силой и ' \
    'направлением ветра, облачностью, атмосферными осадками, дальностью видимости, атмосферными явлениями (туманами, метелями, грозами) и другими метеорологическими ' \
    'элементами. Погода испытывает непрерывные изменения, которые могут быть очень ощутимы не только от одного дня к другому, но и на протяжении даже нескольких минут. ' \
    'Изменения погоды бывают периодические и непериодические. Периодические изменения — это те изменения, которые имеют периодический характер, потому что связаны ' \
    'с вращением Земли вокруг своей оси (суточные изменения) или вокруг Солнца (годовые изменения). Наиболее заметны суточные изменения непосредственно у земной ' \
    'поверхности, в связи с тем, что они определяются изменениями температуры земной поверхности, а с температурой воздуха связаны остальные метеорологические ' \
    'элементы. Годовые изменения выражаются в смене времён года. Непериодические изменения, особенно значительные во внетропических широтах обусловлены переносом ' \
    'воздушных масс. Несовпадения фазы периодических изменений с характером непериодических приводят к наиболее резким изменениям погоды. Воздушные массы при ' \
    'перемещении из одних областей Земли в другие приносят с собой свойственные им характеристики погоды, отличные от ранее существовавших в данном районе. ' \
    'Эти характеристики определяются тем, откуда пришла воздушная масса и какими свойствами в связи с этим она обладает. С высотой интенсивность непериодических ' \
    'изменений погоды в общем уменьшается. Для авиации важен учёт резких усилений ветра и турбулентности, которые связаны со струйными течениями. Обычные погодные ' \
    'явления на Земле — это ветер, облака, атмосферные осадки (дождь, снег, град и т. д.), туманы, грозы, пыльные бури и метели. Более редкие явления включают ' \
    'в себя стихийные бедствия, такие как торнадо и ураганы. Почти все погодные явления происходят в тропосфере (нижняя часть атмосферы). Различия в физических ' \
    'свойствах воздушных масс возникают из-за изменения угла падения солнечных лучей в зависимости от широты и удалённости региона от океанов. Большое различие ' \
    'температур между арктическим и тропическим воздухом является вероятной причиной возникновения высотных струйных течений. Барические образования в средних ' \
    'широтах, такие как внетропические циклоны, образуются, как правило, в результате развития планетарных волн в зоне высотного струйного течения. Эти образования, '\
    'оказывающие основное влияние на изменения погоды, в результате неустойчивости струйных течений, (так называемый цикл индекса) приходят сериями. Поскольку ось ' \
    'вращения Земли наклонена относительно плоскости её орбиты, угол падения солнечных лучей зависит от времени года. В среднем, температура на поверхности Земли ' \
    'изменяется в течение года в пределах ±40 °C. Изменение параметров орбиты, угла наклона оси и угловой скорости вращения Земли влияет на количество и распределение ' \
    'солнечной энергии на планете, являясь основной причиной долгосрочных изменений климата. Различие температур на поверхности земли в свою очередь вызывает разность ' \
    'в поле атмосферного давления. Горячая поверхность нагревает находящийся над ней воздух, расширяет его, понижая давление и плотность воздуха. Горизонтальный ' \
    'градиент давления, действуя совместно с центробежной силой и силой Кориолиса, связанной с вращением Земли, создают ветер, направленный в свободной атмосфере ' \
    'вдоль линий равного давления — изобар. Атмосфера — это сложная система, поэтому незначительные изменения в одной её части могут оказать большое влияние на систему ' \
    'в целом.'

my_str = my_str.lower()
for simbol in '-.,()—':
    my_str = my_str.replace(simbol, ' ')
my_list = my_str.split()

my_dict = {}
for i in my_list:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

sort_my_dict = []
for k, v in my_dict.items():
    sort_my_dict.append((v, k))
sort_my_dict.sort(reverse=True)

for v, k in sort_my_dict[:10]:
    print(f'{k}: {v}')
