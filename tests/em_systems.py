#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    14.03.2016 17:14:23 CET
# File:    em_systems.py

import pytest
import numpy as np

import z2pack

@pytest.fixture(params=np.linspace(-1, 1, 11))
def kz(request):
    return request.param

@pytest.fixture(params=[10**n for n in range(-4, -1)])
def pos_tol(request):
    return request.param

@pytest.fixture
def simple_system():
    return z2pack.em.System(lambda k: np.eye(4))

@pytest.fixture
def simple_line():
    return lambda t: [0, 0, 0]

@pytest.fixture
def simple_surface():
    return lambda s, t: [0, 0, 0]

@pytest.fixture
def weyl_system():
    return z2pack.em.System(lambda k: np.array(
        [
            [k[2], k[0] -1j * k[1]],
            [k[0] + 1j * k[1], -k[2]]
        ]
    ))

@pytest.fixture
def weyl_line(kz):
    return lambda t: [np.cos(t * 2 * np.pi), np.sin(t * 2 * np.pi), kz]

@pytest.fixture
def weyl_surface():
    return z2pack.shapes.Sphere([0, 0, 0], 1.)