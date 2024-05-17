
from injector import Binder
from TrackMyPrice.Core.Application.Contracts.Factories.FormFactories.FormFactory import IFormFactory
from TrackMyPrice.Core.Application.Factory.FormFactory import FormFactory

def ApplicationServicesInject(binder: Binder):
    binder.bind(IFormFactory, to=FormFactory)
    return binder