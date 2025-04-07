'''
Dashboard for displaying static and draft images using Panel for internship project.
It allows users to view and interact with different figures, including static figures 
(e.g., climate maps, climatograms, etc.) and draft plots. 
Users can select specific figures from dropdown menus in the sidebar, 
and the corresponding images will be displayed with their captions and additional information. 
The purpose of this dashboard is to facilitate the visualisations done for my project
'''
############################################### Import necessary libraries ########################################################
import panel as pn
pn.extension('tabulator', sizing_mode="stretch_width")

############################################### Create sidebar buttons and dropdowns ##############################################
def create_button_sidebar(name,description):
    button = pn.widgets.Button(
        name=name,
        button_type="default",
        button_style='outline',
        description=description,
        styles={
            'box-shadow':'0px',
            "font-size": "20px",
            "background-color": "#FFF6E9", 
            "border": "2px solid black", 
            "padding": "3px",
            "width": '35%',
            'border-radius':'10px',
        }
    )
    return button
button_introduction = create_button_sidebar('Introduction', ' ')
button_static = create_button_sidebar('Static Figures', 'Figures 1, 2, 4, 5, 8')
button_draft = create_button_sidebar('Draft Plots', 'View Draft Plots')

# Create widget to display static figures
static_dropdown = pn.widgets.Select(
    name='Select Figure',
    options=['Figure 1', 'Figure 2', 'Figure 4 (Cebu and NCR)', 
            'Figure 5 (Cebu, Cebu City, Manila, NCR)',
            'Figure 8 (Rx1day)', 'Figure 8 (CDD)', 'Figure 8 (CDD Periods)'],
    value='Figure 1',
    width=200,
    align='center',
    styles={
        "background-color": "#FFF6E9",
        "border": "2px solid black",
        "border-radius": "10px",
        "padding": "5px",
        "font-size": "15px",
        "font-weight": "bold",
        "color": "black"
    }
)

# Create widget to display draft plots
draft_dropdown = pn.widgets.Select(
    name='Select Figure',
    options=['Figure 1', 'Figure 2', 'Figure 4'],
    value='Figure 1',
    width=200,
    align='center',
    styles={
        "background-color": "#FFF6E9",
        "border": "2px solid black",
        "border-radius": "10px",
        "padding": "5px",
        "font-size": "15px",
        "font-weight": "bold",
        "color": "black"
    }
)

############################################### Define filepaths to images #######################################################
fig1_png_path = 'static/fig1_combined.png'
fig2_png_path = 'static/Fig2_Number of TCs.png'
fig4_png_path_cebu = 'static/Fig4_Cebu.png'
fig4_png_path_manila = 'static/Fig4_Manila.png'
fig5_png_path_manila = 'static/Fig5_Manila.png'
fig5_png_path_ncr = 'static/Fig5_NCR.png'
fig5_png_path_cebu_city = 'static/Fig5_Cebu City.png'
fig5_png_path_cebu = 'static/Fig5_Cebu.png'
fig8_png_path_philippines_rx1day_mid = 'static/Fig8_Rx1Day_Philippines_Mid_Century.png'
fig8_png_path_philippines_rx1day_end = 'static/Fig8_Rx1Day_Philippines_End_Century.png'
fig8_png_path_phillippines_cdd_mid = 'static/Fig8_CDD_Philippines_Mid_Century.png'
fig8_png_path_phillippines_cdd_end = 'static/Fig8_CDD_Philippines_End_Century.png'
fig8_png_path_philippines_cdd_period_mid = 'static/Fig8_Periods_Philippines_Mid_Century.png'
fig8_png_path_philippines_cdd_period_end = 'static/Fig8_Periods_Philippines_End_Century.png'
fig8_png_path_manila_rx1day_mid = 'static/Fig8_Rx1Day_Manila_Mid_Century.png'
fig8_png_path_manila_rx1day_end = 'static/Fig8_Rx1Day_Manila_End_Century.png'
fig8_png_path_manila_cdd_mid = 'static/Fig8_CDD_Manila_Mid_Century.png'
fig8_png_path_manila_cdd_end = 'static/Fig8_CDD_Manila_End_Century.png'
fig8_png_path_manila_cdd_period_mid = 'static/Fig8_Periods_Manila_Mid_Century.png'
fig8_png_path_manila_cdd_period_end = 'static/Fig8_Periods_Manila_End_Century.png'
fig8_png_path_ncr_rx1day_mid = 'static/Fig8_Rx1Day_NCR_Mid_Century.png'
fig8_png_path_ncr_rx1day_end = 'static/Fig8_Rx1Day_NCR_End_Century.png'
fig8_png_path_ncr_cdd_mid = 'static/Fig8_CDD_NCR_Mid_Century.png'
fig8_png_path_ncr_cdd_end = 'static/Fig8_CDD_NCR_End_Century.png'
fig8_png_path_ncr_cdd_period_mid = 'static/Fig8_Periods_NCR_Mid_Century.png'
fig8_png_path_ncr_cdd_period_end = 'static/Fig8_Periods_NCR_End_Century.png'
fig8_png_path_cebu_rx1day_mid = 'static/Fig8_Rx1Day_Cebu_Mid_Century.png'
fig8_png_path_cebu_rx1day_end = 'static/Fig8_Rx1Day_Cebu_End_Century.png'
fig8_png_path_cebu_cdd_mid = 'static/Fig8_CDD_Cebu_Mid_Century.png'
fig8_png_path_cebu_cdd_end = 'static/Fig8_CDD_Cebu_End_Century.png'
fig8_png_path_cebu_cdd_period_mid = 'static/Fig8_Periods_Cebu_Mid_Century.png'
fig8_png_path_cebu_cdd_period_end = 'static/Fig8_Periods_Cebu_End_Century.png'
fig8_png_path_cebu_city_rx1day_mid = 'static/Fig8_Rx1Day_Cebu_City_Mid_Century.png'
fig8_png_path_cebu_city_rx1day_end = 'static/Fig8_Rx1Day_Cebu_City_End_Century.png'
fig8_png_path_cebu_city_cdd_mid = 'static/Fig8_CDD_Cebu_City_Mid_Century.png'
fig8_png_path_cebu_city_cdd_end = 'static/Fig8_CDD_Cebu_City_End_Century.png'
fig8_png_path_cebu_city_cdd_period_mid = 'static/Fig8_Periods_Cebu_City_Mid_Century.png'
fig8_png_path_cebu_city_cdd_period_end = 'static/Fig8_Periods_Cebu_City_End_Century.png'
fig1_caption = 'captions/Fig1_Caption.png'
fig1_info = 'captions/Fig1_info.png'
fig2_caption = 'captions/Fig2_info.png'
fig2_info = 'captions/Fig2_info_2.png'
fig4_mk = 'captions/MKtest.png'
fig4_caption = 'captions/Fig4_info.png'
fig4_info = 'captions/Fig4_info_2.png'
fig4_mk_info = 'captions/Fig4_info_3.png'
fig5_caption = 'captions/Fig5_caption.png'
fig8_caption = 'captions/Fig8_caption.png'
fig8_caption_2 = 'captions/Fig8_caption_2.png'
fig8_caption_3 = 'captions/Fig8_caption_3.png'
fig8_info = 'captions/Fig8_info.png'

# Draft images
fig1_draft_path = 'drafts/climate_map.png'
fig1_draft_path_climatogram = 'drafts/practice_climatogram.png'
fig1_draft_path_climatogram_2 = 'drafts/climatology_ver2.png'
fig1_draft_caption = 'captions/Fig1_draft_info.png'
fig1_draft_caption_2 = 'captions/Fig1_draft_info_2.png'
fig2_draft_path = 'drafts/TC_frequency.png'
fig2_draft_caption = 'captions/Fig2_draft_info.png'
fig4_draft_path = 'drafts/Fig4_Manila_2.png'
fig4_draft_caption = 'captions/Fig4_draft_info.png'

############################################### Create figures #################################################################
def CreatePage1():
    # Add image for the introduction
    image_path='drafts/Coverslide.png'
    return pn.pane.PNG(image_path, width=1280, height=720)

def staticimage(image_path, caption_path, info_path):
    return pn.Column(
        pn.Row(
            pn.pane.PNG(caption_path, width=500),
            pn.pane.PNG(info_path, width=500)
        ),
        pn.pane.PNG(image_path, width=1280, height=720))

figure1_static = staticimage(fig1_png_path, fig1_caption, fig1_info)
figure2_static = staticimage(fig2_png_path, fig2_caption, fig2_info)
figure4_static = staticimage(fig4_png_path_cebu, fig4_caption, fig4_info)

def fig8_static(caption, info, ph1, ph2, m1, m2, n1, n2, c1, c2, cc1, cc2):
    return pn.Column(
        pn.Row(
            pn.pane.PNG(caption, width=500),
            pn.pane.PNG(info, width=500)
        ),
        pn.Row(
            pn.pane.PNG(ph1, width=640, height=480),
            pn.pane.PNG(ph2, width=640, height=480)
        ),
        pn.Row(
            pn.pane.PNG(c1, width=640, height=480),
            pn.pane.PNG(c2, width=640, height=480)
        ),
        pn.Row(
            pn.pane.PNG(cc1, width=640, height=480),
            pn.pane.PNG(cc2, width=640, height=480)
        ),
        pn.Row(
            pn.pane.PNG(m1, width=640, height=480),
            pn.pane.PNG(m2, width=640, height=480)
        ),
        pn.Row(
            pn.pane.PNG(n1, width=640, height=480),
            pn.pane.PNG(n2, width=640, height=480)
        )
    )

fig8_rx1day_static = fig8_static(
    fig8_caption, fig8_info,
    fig8_png_path_philippines_rx1day_mid, fig8_png_path_philippines_rx1day_end,
    fig8_png_path_cebu_rx1day_mid, fig8_png_path_cebu_rx1day_end,
    fig8_png_path_manila_rx1day_mid, fig8_png_path_manila_rx1day_end,
    fig8_png_path_ncr_rx1day_mid, fig8_png_path_ncr_rx1day_end,
    fig8_png_path_cebu_city_rx1day_mid, fig8_png_path_cebu_city_rx1day_end
)

fig8_cdd_static = fig8_static(
    fig8_caption_2, fig8_info,
    fig8_png_path_phillippines_cdd_mid, fig8_png_path_phillippines_cdd_end,
    fig8_png_path_cebu_cdd_mid, fig8_png_path_cebu_cdd_end,
    fig8_png_path_cebu_city_cdd_mid, fig8_png_path_cebu_city_cdd_end,
    fig8_png_path_manila_cdd_mid, fig8_png_path_manila_cdd_end,
    fig8_png_path_ncr_cdd_mid, fig8_png_path_ncr_cdd_end,
)

fig8_cdd_period_static = fig8_static(
    fig8_caption_3, fig8_info,
    fig8_png_path_philippines_cdd_period_mid, fig8_png_path_philippines_cdd_period_end,
    fig8_png_path_cebu_cdd_period_mid, fig8_png_path_cebu_cdd_period_end,
    fig8_png_path_cebu_city_cdd_period_mid, fig8_png_path_cebu_city_cdd_period_end,
    fig8_png_path_manila_cdd_period_mid, fig8_png_path_manila_cdd_period_end,
    fig8_png_path_ncr_cdd_period_mid, fig8_png_path_ncr_cdd_period_end,
)

def CreatePage2():
    return pn.Column(static_dropdown,
        pn.bind(
            lambda value:
                figure1_static if value == 'Figure 1' else
                figure2_static if value == 'Figure 2' else
                pn.Column(
                    figure4_static,
                    pn.pane.PNG(fig4_png_path_manila, width=1280, height=720),
                    pn.pane.PNG(fig4_mk_info),
                    pn.pane.PNG(fig4_mk, width=1080)
                ) if value == 'Figure 4 (Cebu and NCR)' else
                pn.Column(
                    pn.Row(
                        pn.pane.PNG(fig5_caption, width=500),
                        pn.pane.PNG(fig4_info, width=500)
                    ),
                    pn.Row(
                        pn.pane.PNG(fig5_png_path_cebu, width=640, height=480),
                        pn.pane.PNG(fig5_png_path_cebu_city, width=640, height=480)
                    ),
                    pn.Row(
                        pn.pane.PNG(fig5_png_path_manila, width=640, height=480),
                        pn.pane.PNG(fig5_png_path_ncr, width=640, height=480)
                    ),
                ) if value == 'Figure 5 (Cebu, Cebu City, Manila, NCR)' else
                fig8_rx1day_static if value == 'Figure 8 (Rx1day)' else
                fig8_cdd_static if value == 'Figure 8 (CDD)' else
                fig8_cdd_period_static if value == 'Figure 8 (CDD Periods)' else
                None,
            static_dropdown),
        align='center'
    )

def CreatePage3():
    return pn.Column(draft_dropdown,
        pn.bind(
            lambda value:
                pn.Row(
                    pn.Column(
                        pn.pane.PNG(fig1_draft_caption, align='center'),
                        pn.Row(
                            pn.pane.PNG(fig1_draft_path, height=720, width=400),
                            pn.pane.PNG(fig1_draft_path_climatogram,height=720, width=400)
                        )),
                    pn.Column(
                        pn.pane.PNG(fig1_draft_caption_2, align='center'), 
                        pn.pane.PNG(fig1_draft_path_climatogram_2,height=720, width=640)
                    ),
                    ) if value == 'Figure 1' else
                pn.Column(
                    pn.pane.PNG(fig2_draft_caption, align='center'),
                    pn.pane.PNG(fig2_draft_path, height=720)
                ) if value == 'Figure 2' else
                pn.Column(
                    pn.pane.PNG(fig4_draft_caption, align='center'),
                    pn.pane.PNG(fig4_draft_path, width=1280, height=720)
                ) if value == 'Figure 4' else
                None,
            draft_dropdown),
        align='center'
    )

############################################### Create dashboard #################################################################
mapping = {
    'Introduction': CreatePage1(),
    'StaticImages': CreatePage2(),
    'DraftImages': CreatePage3()
}

# Create sidebar layout
sidebar = pn.Column(
    pn.pane.Markdown('## Navigation', width=200),
    button_static,
    button_draft,
    width=500,
    align='center'
)

# Create main area layout
main_area = pn.Column(
    mapping["Introduction"],
    width=800,
)

def show_page(page_key):
    main_area.clear()
    main_area.append(mapping[page_key])

button_introduction.on_click(lambda event: show_page("Introduction"))
button_static.on_click(lambda event: show_page("StaticImages"))
button_draft.on_click(lambda event: show_page("DraftImages"))

template = pn.template.BootstrapTemplate(
    title=" Eileen's Internship Dashboard - Images",
    sidebar=[sidebar],
    main=[main_area],
    header_background="#B35C3E", 
    sidebar_width=250,
)

# Serve the dashboard
template.servable()