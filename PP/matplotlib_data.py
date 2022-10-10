# import matplotlib.pyplot as plt
# x=[8,10,30,35,45,64,23]
# rt=[0,10,20,30,40,50,60]
# plt.bar(x,rt,color='maroon')
# plt.hist(x,rt,histtype='bar',color="fuchsia")
# plt.show()

# import numpy as np
# print(np.__version__)
# import matplotlib as mp
# print(mp.__version__)


# import numpy as np
# a = np.array([1, 2, 3, 4, 5])
# b = np.array((1, 2, 3, 4, 5))
# c = np.array([1])
# print(a)
# print(b)
# print(c)
# t=[1,2,3,4,5]
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(t))

# import numpy as np
# a = np.array((1, 2, 3, 4, 5))
# b = np.ndarray(())
# print(a)
# print(b)

# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)

# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# arr = np.mat([[1, 2, 3], [4, 5, 6]])
# print(arr)

# import numpy as np
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)



# import matplotlib
# print(matplotlib.__version__)


# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([0, 6])
# y = np.array([0,10])
# plt.plot(x,y)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([1, 8])
# y = np.array([3, 10])
# plt.plot(x, y,'o')
# plt.plot(x, y,'s')
# plt.plot(x, y,'p')
# plt.plot(x, y,'h')
# plt.plot(x,y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([1, 2, 6, 8])
# y = np.array([3, 8, 1, 10])
# plt.plot(x,y)
# plt.plot(x, y,marker='o')
# plt.plot(x, y,'s:k')
# plt.plot(x, y,'s:c')
# plt.plot(x, y,'s:y')
# plt.plot(x, y,'s:w')
# plt.plot(x, y,'s-b')
# plt.plot(x, y,'s--r')
# plt.plot(x, y,'s--g')
# plt.plot(x, y,'s-.m')
# plt.plot(x, y,'s-.g',ms=10, mec='r',mfc='k')
# plt.plot(x, y,ls='dotted')
# plt.plot(x, y,ls='dashdot')
# plt.plot(x, y,ls='dashed')
# plt.plot(x, y,ls='None')
# plt.plot(x, y,ls='solid',lw="0")
# plt.plot(x, y,ls='solid',lw="1")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([1,2,3,4,5])
# y = np.array([10,20,30,40,50])
# font1 = {'family':'TimesNewRoman','color':'blue','size':20}
# font2 = {'family':'Harrington','color':'darkred','size':15}
# plt.title("Course",fontdict = font2)
# plt.xlabel("Python",fontdict = font2)
# plt.ylabel("Adv Python",fontdict = font1)
# plt.plot(x,y)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# font1 = {'family':'TimesNewRoman','color':'blue','size':20}
# plt.ylabel("Adv Python",fontdict = font1)
# plt.pie(y)
# plt.show()

# import matplotlib
# print(dir(matplotlib))

# print(len(['ExecutableNotFoundError', 'MatplotlibDeprecationWarning', 'MutableMapping', 'Parameter', 
# 'Path', 'RcParams', '_ExecInfo', '_VersionInfo', '__bibtex__', '__builtins__', '__cached__', '__doc__', 
# '__file__', '__getattr__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 
# '_add_data_doc', '_all_deprecated', '_api', '_c_internal_utils', '_check_versions', '_cm', '_cm_listed', 
# '_color_data', '_deprecated_ignore_map', '_deprecated_map', '_deprecated_remain_as_none',
# '_ensure_handler', '_enums', '_get_config_or_cache_dir', '_get_executable_info', '_get_ssl_context',
# '_get_version', '_get_xdg_cache_dir', '_get_xdg_config_dir', '_init_tests', '_label_from_arg',
# '_log', '_logged_cached', '_open_file_or_url', '_parse_to_version_info', '_path', '_preprocess_data',
# '_rc_params_in_file', '_replacer', '_version', 'atexit', 'bezier', 'cbook', 'checkdep_usetex',
# 'cm', 'colormaps', 'colors', 'contextlib', 'cycler', 'defaultParams', 'default_test_modules', 
# 'docstring', 'fontconfig_pattern', 'ft2font', 'functools', 'get_backend', 'get_cachedir', 
# 'get_configdir', 'get_data_path', 'importlib', 'inspect', 'interactive', 'is_interactive', 
# 'is_url', 'locale', 'logging', 'matplotlib_fname', 'mplDeprecation', 'namedtuple', 'numpy', 
# 'os', 'parse_version', 'path', 'pprint', 'rc', 'rcParams', 'rcParamsDefault', 'rcParamsOrig',
# 'rc_context', 'rc_file', 'rc_file_defaults', 'rc_params', 'rc_params_from_file', 'rcdefaults', 
# 'rcsetup', 're', 'sanitize_sequence', 'scale', 'set_loglevel', 'shutil', 'subprocess', 'sys', 
# 'tempfile', 'test', 'ticker', 'transforms', 'use', 'validate_backend', 'warnings']))