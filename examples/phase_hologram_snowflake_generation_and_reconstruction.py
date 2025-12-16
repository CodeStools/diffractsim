import diffractsim
diffractsim.set_backend("CPU") #Change the string to "CUDA" to use GPU acceleration

from diffractsim import MonochromaticField, ApertureFromImage, Lens, mm, nm, cm, FourierPhaseRetrieval


# Generate a Fourier plane phase hologram
PR = FourierPhaseRetrieval(target_amplitude_path = './apertures/snowflake.png', new_size= (400,400), pad = (200,200))
PR.retrieve_phase_mask(max_iter = 200, method = 'Conjugate-Gradient')
# PR.save_retrieved_phase_as_image('snowflake_phase_hologram.png')
PR.save_retrieved_phase_as_image('snowflake_phase_hologram.png', phase_mask_format = 'grayscale')


#Add a plane wave
F = MonochromaticField(
    wavelength=632.8 * nm, extent_x=30 * mm, extent_y=30 * mm, Nx=2400, Ny=2400
)

F.add(ApertureFromImage("./apertures/white_background.png", image_size=(10.0 * mm, 10.0 * mm), simulation = F))
F.add(Lens(f = 80*cm))
# for i in range (1, 160, 1):
F.propagate(80*cm)
rgb = F.get_colors()
F.plot_colors(rgb, xlim=[-7* mm, 7* mm], ylim=[-7* mm, 7* mm])
