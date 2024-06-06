
from injector import Binder
from TrackMyPrice.Core.Application.Contracts.Factories.FormFactories.FormFactory import IFormFactory
from TrackMyPrice.Core.Application.Contracts.UnitOfWork import IUnitOfWork
from TrackMyPrice.Core.Application.Contracts.UseCase.ScannedImage_UseCase import IScannedImageCreateUseCase
from TrackMyPrice.Core.Application.Factory.FormFactory import FormFactory
from TrackMyPrice.Core.Application.Persistence.UnitOfWork import UnitOfWork
from TrackMyPrice.Core.Application.UseCases.ImageTrack.ScannedImage_UseCases import ScannedImageCreateUseCase

def ApplicationServicesInject(binder: Binder):
    binder.bind(IFormFactory, to=FormFactory)
    binder.bind(IUnitOfWork, to=UnitOfWork)
    #binder.bind(IScannedImageCreateUseCase, ScannedImageCreateUseCase)
    return binder