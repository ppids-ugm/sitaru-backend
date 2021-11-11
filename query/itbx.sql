CREATE OR REPLACE FUNCTION fnget_itbx(
	fnget_keterangan_tipekegiatan character varying,
	fnget_keterangan_kegiatan character varying,
	fnget_keterangan_subzona character varying)
   RETURNS json AS $$
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
	RETURN izinpemanfaatan::json;
	END;
$$; LANGUAGE 'plpgsql'