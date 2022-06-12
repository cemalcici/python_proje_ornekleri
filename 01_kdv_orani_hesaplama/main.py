"""
İsim: KDV Oranı Hesaplama
Seviye: Başlangıç

Oran seçeneği ve tutar değeri kullanıcıdan alınmıştır.

Bu iki seçeneğe göre tutarın KDV dahil olduğu durumdaki değeri ile KDV hariç olduğu durumdaki değeri hesaplanmaktadır.
"""

cikis_yapild_mi = False

while not cikis_yapild_mi:

    print('[1]:%1', '[8]: %8', '[18]: %18', sep='\n')

    secenek = input('Kdv Oranını Seçiniz (Çıkış için 0): ')

    if secenek == '0':
        print('Program başarıyla sonlandırılmıştır.')
        cikis_yapild_mi = True

    elif secenek == '1' or secenek == '8' or secenek == '18':

        if secenek == '1':
            kdv_orani = 0.01
        elif secenek == '8':
            kdv_orani = 0.08
        elif secenek == '18':
            kdv_orani = 0.18

        tutar = float(input('Tutar Giriniz (Örn 3141.59): '))

        kdv_haric_tutar = tutar / (1 + kdv_orani)
        kdv_dahil_tutar = tutar * (1 + kdv_orani)

        print(tutar, 'KDV hariç tutar ise, KDV dahil tutarı', kdv_dahil_tutar)
        print(tutar, 'KDV dahil tutar ise, KDV hariç tutarı', kdv_haric_tutar)

    else:
        print('Sunulanın dışında KDV oranı girdiniz!')
