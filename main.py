from datetime import date
from dateutil.relativedelta import relativedelta 

class vendor_payment_main_entity:
    def __init__(self,statici_odemeleri):
        self.statici_odemeleri = statici_odemeleri
        self.odeme_tutari_toplam = sum(vendor_payment.odeme_tutari for vendor_payment in self.statici_odemeleri)
        self.simdiki_deger_toplam = sum(vendor_payment.simdiki_deger for vendor_payment in self.statici_odemeleri)
    
    @staticmethod
    def calculate_days_between(date1,date2):
        delta = date1 - date2
        return delta.days
    @staticmethod
    def calculate_present_value(days_between,future_value,gc_yillik):
        present_value = future_value/((1 + gc_yillik/100) ** (days_between/360))
        return present_value
    
    @staticmethod
    def get_gc_yillik():
        return 3.04150
    
    def get_odeme_tutari_toplam(self):
        return self.odeme_tutari_toplam
    
    def get_simdiki_deger_toplam(self):
        return round(self.simdiki_deger_toplam,2)
    
class vendor_payment_entity:
    def __init__(self,odeme_tarihi,odeme_tutari,gun_fark,simdiki_deger):
        self.odeme_tarihi = odeme_tarihi
        self.odeme_tutari = odeme_tutari
        self.gun_fark = gun_fark
        self.simdiki_deger = simdiki_deger
    


class payment_entity:
    def __init__(self,fkt,ov,installments):
        self.gc_yillik = 3.04150
        self.fkt = fkt
        self.r_yillik = 3.01552
        self.r_aylik = self.r_yillik / 12
        self.ov = ov
        self.installments = installments

    @staticmethod
    def add_month(original_date,months_to_add):
        return original_date + relativedelta(months=months_to_add)
    
    @staticmethod
    def calculate_days_between(date1,date2):
        delta = date1 - date2
        return delta.days



def main():

    
    fkt = date(2016,12,12)
    gc_yillik = vendor_payment_main_entity.get_gc_yillik()
     

    vendor_payments = []
    number_mappings = {
        1:(date(2016,12,15),171400.00),
        2:(date(2017,3,1),85700.00),
        3:(date(2017,3,27),85700.00),
        4:(date(2017,4,10),42850.00),
        5:(date(2017,4,24),42850.00),        
    }

    for number in range(1,6):
        vp_odeme_tarihi, vp_odeme_tutari = number_mappings.get(number)       
        vp_gun_fark = vendor_payment_main_entity.calculate_days_between(vp_odeme_tarihi,fkt)
        vp_simdiki_deger = vendor_payment_main_entity.calculate_present_value(vp_gun_fark,vp_odeme_tutari,gc_yillik)
        vp = vendor_payment_entity(vp_odeme_tarihi,vp_odeme_tutari,vp_gun_fark,vp_simdiki_deger)
        vendor_payments.append(vp)
    vendor_payment_main = vendor_payment_main_entity(vendor_payments)
    
    print(vendor_payment_main.get_odeme_tutari_toplam())
    print(vendor_payment_main.get_simdiki_deger_toplam())

    
    number_guncellenen_taksit = {
        1:(4972.00),
        2:(4972.00),
        3:(4972.00),
        4:(4972.00),
        37:(7458.00),
        38:(7458.00),
        39:(7458.00),
        40:(2486.00),    
    }
    number_guncellenen_taksit = {
        1:(4972.00),
        2:(4972.00),
        3:(4972.00),
        4:(4972.00),
        37:(7458.00),
        38:(7458.00),
        39:(7458.00),
        40:(2486.00),    
    }

    installments = []

    for number in range(1,41):
        
        tarih = fkt if number == 1 else payment_entity.add_month(fkt,number)
        gercek_gun = payment_entity.calculate_days_between(tarih, tarih if number == 1 else installments[number - 1].tarih)
        taksit = number_guncellenen_taksit.get(number,(0))
        if taksit == 0:
            taksit 
        installment = installment_entity(number,tarih,gercek_gun)
        installments.append(installment)

class installment_entity:
    def __init(self,no,tarih,gercek_gun,taksit,ap,kar,kalan_ap,guncel_deger_oran,guncellenen_taksit):
        self.no = no
        self.tarih = tarih
        self.gercek_gun = gercek_gun
        self.gun = 30
        self.taksit = taksit
        self.ap = ap
        self.kar = kar
        self.kalan_ap = kalan_ap
        self.guncel_deger_oran = guncel_deger_oran
        self.guncellenen_taksit = guncellenen_taksit
        # self.guncel_deger_oran_x = guncel_deger_x
        
if __name__ == '__main__':
    main()
