Aplikasi SITARU v2 dikembangkan menggunakan PostgreSQL untuk menangani basisdata spasial, non-spasial maupun manajemen akses akun aplikasi. Bahasa yang digunakan adalah SQL. Penggunaan SQL memberikan konsekuensi bahwa setiap data spasial maupaun non-spasial yang dikelola dalam SITARU v2 harus jelas struktur datanya, apa saja kelengkapan atribut data dan bagaimana penulisannya. Apabila terdapat perubahan struktur data dikemudian hari maka harus dilakukan penyesuian pada sisi beckend dan hal ini tidak akan mengganggu sistem yang sudah berjalan. 

File ERD_Matrix_ITBX.pdf dan ERD_Matrix_ITBX.xlsx menyajikan informasi relasi antar tabel yang mendukung SITARU v2. Apabila kedepannya terdapat perubahan regulasi yang mengakibatkan penyesuaian isi dari Matrix ITBX maka dapat langsung diakomodasi dengan mengupdate record/ row pada tabel terkait.

sitaru_db.sql merupakan backup dari database yang berisi tabel tabel ITBX dengan relasinya

# scalar function ITBX Query
CREATE OR REPLACE FUNCTION public.fnget_kodeizin(
	fnget_keterangan_tipekegiatan character varying,
	fnget_keterangan_kegiatan character varying,
	fnget_keterangan_subzona character varying)
    RETURNS character varying
    LANGUAGE 'plpgsql'
AS $$
DECLARE
	izinpemanfaatan character varying;
	BEGIN
		SELECT izin.keterangan_izin into izinpemanfaatan as izin_pemanaatan
		FROM peraturan 
			INNER JOIN tipe_kegiatan on peraturan.kode_tipekegiatan = tipe_kegiatan.kode_tipekegiatan
			INNER JOIN kegiatan on peraturan.kode_tipekegiatan = kegiatan.kode_tipekegiatan and 
				peraturan.id_kegiatan = kegiatan.id_kegiatan
			INNER JOIN sub_zona on peraturan.kode_subzona = sub_zona.kode_subzona
			INNER JOIN zona on sub_zona.kode_zona = zona.kode_zona
			INNER JOIN izin on peraturan.kode_izin = izin.kode_izin
		WHERE fnget_keterangan_tipekegiatan = tipe_kegiatan.keterangan_tipekegiatan
			AND fnget_keterangan_kegiatan = kegiatan.keterangan_kegiatan
			AND fnget_keterangan_subzona = sub_zona.keterangan_subzona;	
	RETURN izinpemanfaatan;
	END;
$$;

# run scalar function ITBX Query (ex: condition for tipe_kegiatan = PENGHIJAUAN and kegiatan = Taman Lingkungan and zona = Cagar Budaya Bersejarah & Pengetahuan)
select fnget_kodeizin('PENGHIJAUAN','Taman Lingkungan','Cagar Budaya Bersejarah & Pengetahuan');
