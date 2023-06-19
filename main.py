from datetime import date

class payment_entity:
    def __init__(self,fkt,ov,installments):
        self.gc_yillik = 3.04150
        self.fkt = fkt
        self.r_yillik = 3.01552
        self.r_aylik = self.r_yillik / 12
        self.ov = ov
        self.installments = installments

class installment_entity:
    def __init(self,no,tarih,gercek_gun,taksit,ap,kar,kalan_ap,guncel_deger_oran):
        self.no = no
        self.tarih = tarih
        self.gercek_gun = gercek_gun
        self.gun = 30
        self.taksit = taksit
        self.ap = ap
        self.kar = kar
        self.kalan_ap = kalan_ap
        self.guncel_deger_oran = guncel_deger_oran
        # self.guncel_deger_oran_x = guncel_deger_x

class vendor_payment_main_entity:
    def __init__(self):
        self.statici_odemeleri
        self.odeme_tutari_toplam
        self.simdiki_deger_toplam
    
    @staticmethod
    def calculate_days_between(self,date1,date2):
        delta = date1 - date2
        return delta.days
    
class vendor_payment_entity:
    def __init__(self,odeme_tarihi,odeme_tutari,gun_fark,simdiki_deger):
        self.odeme_tarihi = odeme_tarihi
        self.odeme_tutari = odeme_tutari
        self.gun_fark = gun_fark
        self.simdiki_deger = simdiki_deger
    

def main():
    fkt = date(2016,12,12)
    vp1_odeme_tarihi = date(2016,12,15)
    vp1_odeme_tutari = 171400.00
    vp1_gun_fark = vendor_payment_entity.calculate_days_between(vp1_odeme_tarihi,fkt)
    vp1

    vp1 = vendor_payment_entity(vp1_odeme_tarihi,vp1_odeme_tutari,vp1_gun_fark,)

    payment = payment_entity()

if __name__ == '__main__':
    main()
