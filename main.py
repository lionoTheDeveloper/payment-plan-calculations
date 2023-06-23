from datetime import date,datetime,timedelta
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
  
    
    first_vendor_payment_date,_ = number_mappings.get(1)
    ov = first_vendor_payment_date
    ov_denominator = 0.00
    vp_days = 0.00
    for number,vendor_payment in number_mappings.items():
        vp_odeme_tarihi, vp_odeme_tutari = vendor_payment       
        vp_gun_fark = vendor_payment_main_entity.calculate_days_between(vp_odeme_tarihi,fkt)
        vp_simdiki_deger = vendor_payment_main_entity.calculate_present_value(vp_gun_fark,vp_odeme_tutari,gc_yillik)
        vp = vendor_payment_entity(vp_odeme_tarihi,vp_odeme_tutari,vp_gun_fark,vp_simdiki_deger)
        ov_denominator += vp_odeme_tutari
        vp_days += vp_odeme_tutari * (vp_odeme_tarihi - first_vendor_payment_date).days        
        vendor_payments.append(vp)
    vendor_payment_main = vendor_payment_main_entity(vendor_payments)    
    ov_real_days =  vp_days/ov_denominator
    ov = ov + relativedelta(days=ov_real_days)
    
    number_guncellenen_taksit = {
        1:(4972.00),
        2:(4972.00),
        3:(4972.00),
        4:(9944.00),
        37:(7458.00),
        38:(7458.00),
        39:(7458.00),
        40:(2486.00),    
    }
    #   number_guncellenen_taksit = {
    #     1:(4972.00),
    #     2:(4972.00),
    #     3:(4972.00),
    #     4:(4972.00),
    #     37:(7458.00),
    #     38:(7458.00),
    #     39:(7458.00),
    #     40:(2486.00),    
    # }

    installments = []
    
    installment_count = 40
    for number in range(0,installment_count):        
        tarih = fkt if number == 0 else payment_entity.add_month(fkt,(number) )
        gercek_gun = payment_entity.calculate_days_between(tarih, tarih if number == 0 else installments[number - 1].tarih)
        taksit = number_guncellenen_taksit.get((number + 1),(0.00))
        installment = installment_entity((number + 1),tarih,gercek_gun,taksit,0,0,0,taksit)                
        installments.append(installment)
    
    payment = payment_entity(fkt,ov,installments,vendor_payment_main)
   
    # print(payment.get_annuity_amount())
    # print(vendor_payment_main.get_odeme_tutari_toplam())
    # print(vendor_payment_main.get_simdiki_deger_toplam())
    for installment_final in payment.installments:
        print(installment_final)

class payment_entity:
    def __init__(self,fkt,ov,installments,vendor_payment_main):
        self.gc_yillik = 3.04150
        self.fkt = fkt
        self.r_yillik = 3.01552
        self.r_aylik = self.r_yillik / 12
        self.ov = ov
        self.installments = installments
        self.vendor_payment_main = vendor_payment_main
        self.get_installments_after_final_calculation()
   
    @staticmethod
    def add_month(original_date,months_to_add):
        return original_date + relativedelta(months=months_to_add)
    
    @staticmethod
    def calculate_days_between(date1,date2):
        delta = date1 - date2
        return delta.days
    
    @staticmethod
    def get_r_yilik():
        return 3.01552
    
   
    def get_annuity_amount(self):
        total_present_value_rate = 0.00
        total_present_value_guncellenen_taksit = 0.00
        total_present_value_diff = 0.00
        for installment in self.installments:
            total_present_value_rate += 0.00 if installment.guncellenen_taksit != 0.00 else installment.calculated_present_value_rate
            total_present_value_guncellenen_taksit += installment.guncellenen_taksit_present_value  
        total_present_value_guncellenen_taksit = round(total_present_value_guncellenen_taksit,2)
        total_present_value_diff = self.vendor_payment_main.get_simdiki_deger_toplam() - total_present_value_guncellenen_taksit
        return round(total_present_value_diff / total_present_value_rate ,2)
    
    def get_installments_after_final_calculation(self):
        annuity_amount = self.get_annuity_amount()
        total_principal_amount = self.vendor_payment_main.get_simdiki_deger_toplam() 
        
        for installment in self.installments:
            if installment.taksit == 0:
                installment.taksit = annuity_amount
            installment.kar = total_principal_amount * ((1 + self.r_aylik / 100) ** (installment.no -1) - 1)  if installment.no == 1 else self.installments[(installment.no - 1)].kalan_ap * ((1 + self.r_aylik / 100) ** (installment.no - 1) - 1)       
            installment.ap = installment.taksit - installment.kar
            installment.kalan_ap = total_principal_amount - installment.ap if installment.no == 1 else self.installments[(installment.no - 1)].kalan_ap - installment.ap
            
class installment_entity:
    def __init__(self,no,tarih,gercek_gun,taksit,ap,kar,kalan_ap,guncellenen_taksit):
        self.no = no
        self.tarih = tarih
        self.gercek_gun = gercek_gun
        self.gun = 30
        self.taksit = taksit
        self.ap = ap
        self.kar = kar
        self.kalan_ap = kalan_ap        
        self.guncellenen_taksit = guncellenen_taksit
        self.calculated_present_value_rate = get_calculated_present_value_rate(self)
        self.guncellenen_taksit_present_value = self.calculated_present_value_rate * self.guncellenen_taksit
        # self.guncel_deger_oran_x = guncel_deger_x

def get_calculated_present_value_rate(self):
    r_aylik = payment_entity.get_r_yilik() / 12
    return 1 / (1 + r_aylik/100 ) ** (self.no - 1)

@property
def guncellenen_taksit_present_value(self):
    return self.guncellenen_taksit_present_value

@guncellenen_taksit_present_value.setter
def guncellenen_taksit_present_value(self,value):
    self.guncellenen_taksit_present_value = value


if __name__ == '__main__':
    main()
