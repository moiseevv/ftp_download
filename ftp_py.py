import ftplib,os
import codecs

def download_serv(serv):
    ftp = ftplib.FTP(serv)
    ftp.login('***', '****')
    ftp.retrlines('LIST')
    
    out = r"D:\ftp_2\ftp\qq"
    
    filenames = ftp.nlst()
    
    for filename in filenames:
        if 'cadastr' in filename:
            host_file = os.path.join(out, filename)
            print('Скачивание - ', host_file)
            try:
                with open(host_file,'wb') as local_file:
                    ftp.retrbinary('RETR '+filename, local_file.write)
            except ftplib.error_perm:
                print('!!! Произошла ОШИБКА ')
    
    
    ftp.quit()



if __name__ == '__main__':
    mas_comp = ['192.168.***.***','192.168.***.***','192.168.***.***','192.168.***.***']
    
    for serv in mas_comp:
        download_serv(serv)