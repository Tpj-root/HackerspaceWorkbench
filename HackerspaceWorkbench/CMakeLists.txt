set(Namespace_SRCS
        freecad/hacker_space_workbench/init_gui.py
        freecad/hacker_space_workbench/__init__.py
        freecad/hacker_space_workbench/my_numpy_function.py
        freecad/hacker_space_workbench/version.py
        freecad/hacker_space_workbench/resources/cool.svg
        freecad/hacker_space_workbench/resources/translations/hacker_space_workbench_es-ES.qm
        freecad/hacker_space_workbench/resources/translations/hacker_space_workbench_es-ES.ts
)

SOURCE_GROUP("" FILES ${Namespace_SRCS})

ADD_CUSTOM_TARGET(SEARCHBAR ALL
        SOURCES ${Namespace_SRCS}
)

fc_copy_sources(SEARCHBAR "${CMAKE_BINARY_DIR}/Mod/HackerspaceWorkbench" ${Namespace_SRCS})

INSTALL(
    FILES
        ${Namespace_SRCS}
    DESTINATION
        Mod/SearchBar
)
