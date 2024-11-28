import AMPLITUDE_FETCHER, AMPLITUDE_TO_PIXEL_VALS, COMPRESSOR, AMP_TO_IMAGE

# GETTING AMPLITUDE
amp_arr = COMPRESSOR.COMPRESSED_ARR_FETCH()
print(amp_arr)
pixel_val_arr = AMPLITUDE_TO_PIXEL_VALS.amp_to_pixel(amp_arr)



AMP_TO_IMAGE.make_image(pixel_val_arr)

