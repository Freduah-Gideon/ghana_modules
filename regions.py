
class RegionsLibrary:
    def __init__(self):
        pass

    def region_list(self):
        region = {
            "region__list": (
                ('AR', 'Ashanti Region'),
                ('BR', 'Bono Region'),
                ('BER', 'Bono East Region'),
                ('AHR', 'Ahafo Region'),
                ('CR', 'Central Region'),
                ('ER', 'Eastern Region'),
                ('GAR', 'Greater Accra Region'),
                ('NR', 'Northern Region'),
                ('SVR', 'Savannah Region'),
                ('NER', 'North East'),
                ('UER', 'Upper East'),
                ('UWR', 'Upper West'),
                ('VR', 'Volta Region'),
                ('OR', 'Oti Region'),
                ('WR', 'Western Region'),
                ('WNR', 'Western North')
            ),
        }
    
    def district_list(self):
        district__list = {
                "ar__list": (
                    ('Adansi North District', 'Adansi North District'),
                    ('Adansi South District', 'Adansi South District'),
                    ('Afigya-Kwabre District', 'Afigya-Kwabre District'),
                    ('Ahafo Ano North Municipal', 'Ahafo Ano North Municpal'),
                    ('Ahafo Ano South District', 'Ahafo Ano South District'),
                    ('Amansie Central District', 'Amansie Central District'),
                    ('Amansie West District', 'Amansie West District'),
                    ('Asante-Akim Central Municipal',
                     'Asante-Akim Central Municipal'),
                    ('Asante Akim North District', 'Asante Akim North District'),
                    ('Asante Akim South Municipal', 'Asante Akim South Municipal'),
                    ('Asokore Mampong Municipal', 'Asokore Mampong Municipal'),
                    ('Atwima Kwanwoma District', 'Atwima Kwanwoma District'),
                    ('Atwima Mponua District', 'Atwima Mponua District'),
                    ('Atwima Nwabiagya Municipal', 'Atwima Nwabiagya Municipal'),
                    ('Bekwai Municipal', 'Bekwai Municipal'),
                    ('Bosome Freho District', 'Bosome Freho District'),
                    ('Botsomtwe District', 'Botsomtwe District'),
                    ('Ejisu-Juaben Municipal', 'Ejisu-Juaben Municipal'),
                    ('Ejura-Sekyedumase Municipal', 'Ejura-Sekyedumase Municipal'),
                    ('Kumasi Metropolitan', 'Kumasi Metropolitan'),
                    ('Kwabre East District', 'Kwabre East District'),
                    ('Mampong Municipal', 'Mampong Municipal'),
                    ('Obuasi Municipal', 'Obuasi Municipal'),
                    ('Offinso North District', 'Offinso North District'),
                    ('Offinso South Municipal', 'Offinso South Municipal'),
                    ('Sekyere Afram Plains District',
                     'Sekyere Afram Plains District'),
                    ('Sekyere Central District', 'Sekyere Central District'),
                    ('Sekyere East District', 'Sekyere East District'),
                    ('Sekyere Kumawu District', 'Sekyere Kumawu District'),
                    ('Sekyere South District', 'Sekyere South District'),
                    ('Suame Municipal', 'Suame Municipal')
                ),
                "br__list": (
                    ('Banda District', 'Banda District'),
                    ('Berekum East Municipal', 'Berekum East Municipal'),
                    ('Berekum West Municipal', 'Berekum West Municipal'),
                    ('Dormaa Central Municipal', 'Dormaa Central Municipal'),
                    ('Dormaa East District', 'Dormaa East District'),
                    ('Dormaa West District', 'Dormaa West District'),
                    ('Jaman North District', 'Jaman North District'),
                    ('Jaman South Municipal', 'Jaman South Municipal'),
                    ('Sunyani Municipal', 'Sunyani Municipal'),
                    ('Sunyani West District', 'Sunyani West District'),
                    ('Tain District', 'Tain District'),
                    ('Wenchi Municipal', 'Wenchi Municipal')
                ),
                "ber__list": (
                    ('Atebubu-Amantin Municipal', 'Atebubu-Amantin Municipal'),
                    ('Kintampo North Municipal', 'Kintampo North Municipal'),
                    ('Kintampo South District', 'Kintampo South District'),
                    ('Nkoranza North District', 'Nkoranza North District'),
                    ('Nkoranza South District', 'Nkoranza South District'),
                    ('Pru East District', 'Pru East District'),
                    ('Pru West District', 'Pru West District'),
                    ('Sene East District', 'Sene East District'),
                    ('Sene West District', 'Sene West District'),
                    ('Techiman Municipal', 'Techiman Municipal'),
                    ('Techiman North District', 'Techiman North District')
                ),
                "cr__list":(
                    ('Abura/Asebu/Kwamankese District','Abura/Asebu/Kwamankese District'),
                    ('Agona East District','Agona East District'),
                    ('Agona West Municipal','Agona West Municipal')
                ),
                "gar__list": (
                    ('Accra Metropolitan', 'Accra Metropolitan'),
                    ("Ada East District", 'Ada East District'),
                    ("Ada West District", 'Ada West District'),
                    ('Adenta Municipal', 'Adenta Municipal'),
                    ('Ashaiman Municipal', 'Ashaiman Municipal'),
                    ('Ga Central Municipal', 'Ga Central Municipal'),
                    ('Ga East Municipal', 'Ga East Municipal'),
                    ('Ga South Municipal', 'Ga South Municipal'),
                    ('Ga West Municipal', 'Ga West Municipal'),
                    ('Kpone Katamanso District', 'Kpone Katamanso District'),
                    ('La Dade Kotopon Municipal', 'La Dade Kotopon Municipal'),
                    ('La Nkwantanang Madina Municipal',
                     'La Nkwantanang Madina Municipal'),
                    ('Ledzokuku Municipal', 'Ledzokuku Municipal'),
                    ('Krowor Municipal', 'Krowor Municipal'),
                    ('Ningo Prampram District', 'Ningo Prampram District'),
                    ('Shai Osudoku District', 'Shai Osudoku District'),
                    ('Tema Metropolitan', 'Tema Metropolitan')
                ),
                "nr__list": (
                    ("Gusheigu District", 'Gusheigu District'),
                    ("Karaga District", "Karaga District"),
                    ("Kpandai District", "Kpandai District"),
                    ("Kumbungu District", "Kumbungu District"),
                    ("Miom District", "Mion District"),
                    ("Nanton District", "Nanton District"),
                    ("Nanumba North Municipal", 'Nanumba North Municipal'),
                    ("Nanumba South District", "Nanumba South District"),
                    ("Saboba District", "Saboba District"),
                    ("Sagnarigu Municipal", "Sagnarigu Municipal"),
                    ("Savelugu-Nanton District", "Savelugu-Nanton District"),
                    ("Tamale Metropolitan", "Tamale Metropolitan"),
                    ("Tatale-Sangule District", "Tatale-Sangule District"),
                    ("Yendi Municipal", "Yendi Municipal"),
                    ("Zabzugu District", "Zabzugu District")
                ),
                "ner__list": (
                    ('Bunkpurugu-Nyankpanduri District',
                     'Bunkpurugu-Nyankpanduri District'),
                    ('Chereponi District', 'Chereponi District'),
                    ('East Mamprusi Municipal Assembly',
                     'East Mamprusi Municipal Assembly'),
                    ('Mamprugu Moaduri District', 'Mamprugu Moaduri District'),
                    ('West Mamprusi Municipal District',
                     'West Mamprusi Municipal District'),
                    ('Yunyoo-Nasuan District', 'Yunyoo-Nasuan District')
                ),
                'or__list': (
                    ('Biakoye District', 'Biakoye District'),
                    ('Jasikan District', 'Jasikan District'),
                    ('Kadjebi District', 'Kadjebi District'),
                    ('Krachi East Municipal', 'Krachi East Municipal'),
                    ('Krachi Nchumuru District'),
                    ('Krachi West District'),
                    ('Krachi North District'),
                    ('Nkwanta South Municipal')
                ),
                "svr__list": (
                    ('Bole District', 'Bole District'),
                    ('Central Gonja District', 'Central Gonja District'),
                    ('East Gonja Municipal', 'East Gonja Municipal'),
                    ('North Gonja District', 'North Gonja District'),
                    ('Sawla-Tuna-Kalba District', 'Sawla-Tuna-Kalba District'),
                    ('Tolon District', 'Tolon District'),
                    ('West Gonja', 'West Gonja')
                ),
                "uer__list": (
                    ('Bawku Municipal', 'Bawku Municipal'),
                    ('Bawku West District', 'Bawku West District'),
                    ('Binduri District', 'Binduri District'),
                    ('Bolgatanga Municipal', 'Bolgatanga Municipal'),
                    ('Bongo District', 'Bongo District'),
                    ('Builsa North District', 'Builsa North District'),
                    ('Builsa South District', 'Builsa South District'),
                    ('Garu-Tempane District', 'Garu-Tempane District'),
                    ('Kassena Nankana East Municipal',
                     'Kassena Nankana East Municipal'),
                    ('Kassena Nankana West Municipal',
                     'Kassena Nankana West Municipal'),
                    ('Nabdam District', 'Nabdam District'),
                    ('Pusiga District', 'Pusiga District'),
                    ('Talensi District', 'Talensi District')
                ),
                'uwr__list': (
                    ('Daffiama-Bussie-Issa District',
                     'Daffiama-Bussie-Issa District'),
                    ('Jirapa Municipal', 'Jirapa Municipal'),
                    ('Lambussie Karni District', 'Lambussie Karni District'),
                    ('Lawra Municipal', 'Lawra Municipal'),
                    ('Nadowli-Kaleo District', 'Nadowli-Kaleo District'),
                    ('Nandom District', 'Nandom District'),
                    ('Sissala East Municipal', 'Sissala East Municipal'),
                    ('Sissala West District', 'Sissala West District'),
                    ('Wa East District', 'Wa East District'),
                    ('Wa Municipal', 'Wa Municipal'),
                    ('Wa West District', 'Wa West District')
                ),
                "vr__list": (
                    ('Adaklu District', 'Adaklu District'),
                    ('Afadjato South District', 'Afadjato South District'),
                    ('Agotime Ziope District', 'Agotime Ziope District'),
                    ('Akatsi North District', 'Akatsi North District'),
                    ('Akatsi South District', 'Akatsi South District'),
                    ('Anloga District', 'Anloga District'),
                    ('Central Tongu District', 'Central Tongu District'),
                    ('Ho Municipal', 'Ho Municipal'),
                    ('Ho West District', 'Ho West District'),
                    ('Hohoe Municipal', 'Hohoe Municipal'),
                    ('Keta Municipal', 'Keta Municipal'),
                    ('Ketu North Municipal District',
                     'Ketu North Municipal District'),
                    ('Ketu South Municipal', 'Ketu South Municipal'),
                    ('Kpando Municipal District', 'Kpando Municipal District'),
                    ('North Dayi District', 'North Dayi District'),
                    ('North Tongu District', 'North Tongu District'),
                    ('South Dayi District', 'South Dayi District'),
                    ('South Tongu District', 'South Tongu District')
                ),
                "wr__list": (
                    ('Ahanta West Municipal', 'Ahanta West Municipal'),
                    ('Ellembele Municipal', 'Ellembele Municipal'),
                    ('Jomoro Municipal', 'Jomoro Municipal'),
                    ('Mpohor District', 'Mpohor District'),
                    ('Nzema East Municipal', 'Nzema East Municipal'),
                    ('Prestea-Huni Valley Municipal',
                     'Prestea-Huni Valley Municipal'),
                    ('Sekondi Takoradi Metropolitan',
                     'Sekondi Takoradi Metropolitan'),
                    ('Shama District', 'Shama District'),
                    ('Tarkwa-Nsuaem Municipal', 'Tarkwa-Nsuaem Municipal'),
                    ('Wassa Amenfi Central District',
                     'Wassa Amenfi Central District'),
                    ('Wasa Amenfi East Municipal', 'Wasa Amenfi East Municipal'),
                    ('Wasa Amenfi West Municipal', 'Wasa Amenfi West Municipal'),
                    ('Wassa East District', 'Wassa East District')
                ),
                "wnr__list": (
                    ('Aowin Municipal', 'Aowing Municipal'),
                    ('Bia West District', 'Bia West District'),
                    ('Bia East District', 'Bia East District'),
                    ('Bibiani/Anhwiaso/Bekwai Municipal',
                     'Bibiani/Anhwiaso/Bekwai Municipal'),
                    ('Bodi District', 'Bodi District'),
                    ('Juaboso District', 'Juaboso District'),
                    ('Sefwi Akontambra District', 'Sefwi Akontombra District'),
                    ('Sefwi Wiawso Municipal', 'Sefwi Wiawso Municipal'),
                    ('Suaman District', 'Suaman District')
                )
            }
        



regions = RegionsLibrary()
print(regions.region_list)