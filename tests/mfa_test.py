import numpy as np
import json

from pymultifracs.wavelet import wavelet_analysis
from pymultifracs.estimation import estimate_hmin
from pymultifracs.mfa import mf_analysis_full


def test_mfa_fbm(fbm_file):

    for i, fname in enumerate(fbm_file):

        with open(fname, 'rb') as f:
            X = np.load(f)

        with open('tests/fbm_config.json', 'rb') as f:
            config_list = json.load(f)

        j2 = np.log2(config_list[i]['shape']) - 1
        wt_coefs, _, j2_eff = wavelet_analysis(X, p_exp=None, j2=j2)
        hmin = estimate_hmin(wt_coefs, j1=1, j2_eff=j2_eff, weighted=True)[0]
        hmin = hmin.min()
        gamint = 0.0 if hmin >= 0 else -hmin + 0.1
        dwt, lwt = mf_analysis_full(X, j1=3, j2=j2_eff, gamint=gamint,
                                    p_exp=np.inf, n_cumul=3)
        assert abs(dwt.structure.H.mean() - config_list[i]['H']) < 0.3
        assert abs(lwt.cumulants.log_cumulants[1, :].mean()) < 0.1

        _, lwt = mf_analysis_full(X, j1=3, j2=j2_eff, gamint=gamint, p_exp=2,
                                  n_cumul=3)
        assert abs(lwt.cumulants.log_cumulants[1, :].mean()) < 0.1


def test_mfa_mrw(mrw_file):

    for i, fname in enumerate(mrw_file):

        with open(fname, 'rb') as f:
            X = np.load(f)

        with open('tests/mrw_config.json', 'rb') as f:
            config_list = json.load(f)

        j2 = np.log2(config_list[i]['shape']) - 1
        wt_coefs, _, j2_eff = wavelet_analysis(X, p_exp=None, j2=j2)
        hmin = estimate_hmin(wt_coefs, j1=1, j2_eff=j2_eff, weighted=True)[0]
        hmin = hmin.min()
        gamint = 0.0 if hmin >= 0 else -hmin + 0.1
        dwt, lwt = mf_analysis_full(X, j1=3, j2=j2_eff, gamint=gamint,
                                    p_exp=np.inf, n_cumul=3)
        assert abs(dwt.structure.H.mean() - config_list[i]['H']) < 0.3
        assert abs(lwt.cumulants.log_cumulants[1, :].mean()
                   - (config_list[i]['lam'] ** 2)) < 0.2

        mf_analysis_full(X, j1=3, j2=j2_eff, gamint=gamint, p_exp=2,
                         n_cumul=3)
        assert abs(lwt.cumulants.log_cumulants[1, :].mean()
                   - (config_list[i]['lam'] ** 2)) < 0.2
