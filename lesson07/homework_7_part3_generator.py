import matplotlib.pyplot as plt
import cmocean
import cartopy
import cartopy.crs as ccrs
import os
import xarray as xr

def generate_frame(i):
    
    plt.ioff()
    
    TCW = f'/N/project/easg690_fall2025/data/ERA5/ds633.0/e5.oper.an.sfc/202106/e5.oper.an.sfc.128_136_tcw.ll025sc.2021060100_2021063023.nc' #reads in file
    MSL = f'/N/project/easg690_fall2025/data/ERA5/ds633.0/e5.oper.an.sfc/202106/e5.oper.an.sfc.128_151_msl.ll025sc.2021060100_2021063023.nc'
    
    tcw_Opened_File = xr.open_dataset(TCW, chunks = -1) #opens file and assigns variable to data
    msl_Opened_File = xr.open_dataset(MSL, chunks = -1) #opens file 2 and assigns variable to data
    tcw_at_time_i = tcw_Opened_File.isel(time=i) #creates a variable for TCW data at a specific timestep
    msl_at_time_i = msl_Opened_File.isel(time=i) #creates a variable for MSL data at a specific timestep
    

    # set the projection as frame of reference for figure
    projection = ccrs.Orthographic(central_longitude=-86.5386, central_latitude=39.1696,globe=None)
    
    #I used ChatGPT to help me adapt/debug the function from lesson 6 that froduced a 2x2 figure
    
    # generate a 1x2 panel figure with a better aspect ratio
    fig, axes = plt.subplots(1,2,
                    figsize = (12, 6),
                    sharex = True,
                    sharey = True,
                    subplot_kw = dict(projection = projection),
    )

    tcw_at_time_i['TCW'].plot(ax=axes[0], #georeferences the projection 
                                transform=ccrs.PlateCarree(), #establishes coordinate system
                                cmap=cmocean.cm.rain, #Maps data onto projection
                                cbar_kwargs={'label': 'Precipitable Water (mm)'} #labels colorbar
    )#used chat gpt for this .plot call

    axes[0].coastlines() #displays coastlines in reference to projection
    axes[0].set_title('Total Column Water') #Titles TCW frame
    
    msl_at_time_i['MSL'].plot(ax=axes[1],  # change 'MSL' to the correct variable name in TCW_2
                               transform=ccrs.PlateCarree(),
                               cmap=cmocean.cm.rain,
                               cbar_kwargs={'label': 'Mean Sea Level (Pa)'}
                            )  # adjust label
    axes[1].coastlines()
    axes[1].set_title('Mean Sea Level Pressure')
    
    #I used chatgpt to help me debug and write these lines
    output_dir = '/geode2/home/u015/bpgibbs/Quartz/lesson07/animate_two_pannels'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"tcw_{i:03d}.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)