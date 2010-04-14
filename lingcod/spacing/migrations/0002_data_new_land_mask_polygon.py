from lingcod.spacing.models import Land, create_pickled_graph
from south.v2 import SchemaMigration
from django.contrib.gis import geos

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        l = Land.objects.all()[0]
        l.geometry = geos.fromstr('POLYGON ((255911.2599722782906611 78225.2002380010671914, -268260.2062655743793584 40762.6166391894221306, -322186.8222449655877426 107311.0374853634275496, -318353.7696663595270365 120179.5609497125260532, -329426.3165856546256691 155000.5907706690486521, -323130.5491130823502317 178956.9005401681642979, -327467.8165412769885734 196236.8273245591262821, -328189.6255076351808384 207828.2489266227930784, -333850.9476872601662762 211936.2848368243721779, -343379.2401924693258479 230066.8835292924777605, -347752.0896140428958461 230679.0222805702069309, -348245.3015540605410933 238229.6523473746783566, -370859.3244322579121217 257844.0183260625344701, -368581.6985579121392220 268867.5290421533281915, -374435.6505553201423027 278310.4402883013244718, -343486.4802722530439496 339937.1297304246108979, -347224.8577002387610264 345386.6255582721205428, -348971.7877338045509532 345323.8616049703559838, -349755.0350513913435861 354594.0764322991599329, -348017.9085027888650075 354737.8386294249212369, -341056.3874521552352235 373667.7737405784428120, -339228.4814624458085746 389617.0434157242998481, -345132.6366112539544702 419740.9610317861661315, -354316.6667222678079270 425867.6019557655672543, -349805.4421512550325133 433392.5098101077601314, -348983.2389619935420342 449927.5429992806166410, -365001.3400947164045647 478199.5691306656226516, -361909.7410555686219595 519845.8950312500819564, -373823.4704640990239568 543662.4228328466415405, 241446.4603079776861705 887569.5247417520731688, 255911.2599722782906611 78225.2002380010671914))')
        l.save()
        create_pickled_graph()
            
    def backwards(self, orm):
        l = Land.objects.all()[0]
        l.geometry = geos.fromstr('POLYGON ((255911.2599722782906611 78225.2002380010671914, -268260.2062655743793584 40762.6166391894221306, -272019.5894324489636347 50868.0711503070779145, -286950.7276521701714955 64023.6666701333597302, -305739.3681111233890988 88094.0116850184276700, -322186.8222449655877426 107311.0374853634275496, -318353.7696663595270365 120179.5609497125260532, -328243.1639626394025981 154606.2065629973076284, -322262.9038562045316212 177063.8563433438539505, -324141.5595629107556306 192176.8371892003342509, -328189.6255076351808384 207828.2489266227930784, -341873.0968703787657432 227540.3433088660240173, -348796.7946760837221518 239154.7764930278062820, -369373.3865143205621280 256977.2212072657421231, -368210.2140784277580678 265276.5124071380123496, -372454.3999980703229085 277443.6431695045903325, -345839.2153089871862903 336593.7694150656461716, -348494.3343541029607877 353442.3300207378342748, -341056.3874521552352235 373667.7737405784428120, -339228.4814624458085746 389617.0434157242998481, -345132.6366112539544702 419740.9610317861661315, -353879.0274724643095396 425867.6019557655672543, -349805.4421512550325133 433392.5098101077601314, -348983.2389619935420342 449927.5429992806166410, -360559.8832224382204004 461660.6582783339545131, -365001.3400947164045647 478199.5691306656226516, -365929.7492793372366577 498621.2968536550179124, -361501.2787856945069507 512101.8849661191925406, -361909.7410555686219595 519845.8950312500819564, -373823.4704640990239568 543662.4228328466415405, -367093.4089155389810912 556972.7940391954034567, 241446.4603079776861705 887569.5247417520731688, 255911.2599722782906611 78225.2002380010671914))')
        l.save()
        create_pickled_graph()
